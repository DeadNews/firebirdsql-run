"""Firebirdsql wrapper inspired by subprocess.run."""

from pathlib import Path
from socket import getfqdn

from firebirdsql import (
    Connection,
    connect,
)

from firebirdsql_run.type import CompletedTransaction, DBAccess
from firebirdsql_run.util import Timer, get_env


def connection(
    db: Path | str,
    host: str = "127.0.0.1",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str = "",
    access: DBAccess = DBAccess.READ_WRITE,
) -> Connection:
    """Create a connection to a Firebird database using the firebirdsql library.

    Args:
        db: The path or name of the database.
        host: The host address of the server.
        port: The port number of the server.
        user: The username for authentication.
        passwd: The password. If omitted, it is taken from `FIREBIRD_KEY` environment variable.
        access: The access mode for the connection.

    Returns:
        conn: The connection object.
    """
    return connect(
        host=getfqdn(host),
        database=f"{db}",
        port=port,
        user=user,
        password=passwd or get_env("FIREBIRD_KEY"),
        isolation_level=access.value,
    )


def execute(
    query: str,
    params: tuple = (),
    db: Path | str = "",
    host: str = "127.0.0.1",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str = "",
    access: DBAccess = DBAccess.READ_WRITE,
    use_conn: Connection | None = None,
) -> CompletedTransaction:
    """Execute a transaction in a Firebird database.

    Args:
        query: The SQL query to execute.
        params: The parameters to be used in the query.
        db: The path or name of the database.
        host: The host address of the server.
        port: The port number of the server.
        user: The username for authentication.
        passwd: The password. If omitted, it is taken from `FIREBIRD_KEY` environment variable.
        access: The access mode for the connection.
        use_conn: An existing connection to use. Takes precedence over the default connection settings.

    Returns:
        result: An named tuple containing the transaction details, including the query result.
    """
    conn: Connection | None = None
    timer: Timer | None = None

    try:
        conn = use_conn or connection(
            host=host,
            db=db,
            port=port,
            user=user,
            passwd=passwd,
            access=access,
        )
        with conn.cursor() as cur, Timer() as timer:
            cur.execute(query=query, params=params)
            lines = cur.fetchall()
            descr = cur.description

    except Exception as e:  # noqa: BLE001
        data = []
        returncode = 1
        exception = f"{e}"
    else:
        columns = [] if descr is None else [f"{col[0]}".lower() for col in descr]
        data = [] if lines is None else [dict(zip(columns, line, strict=True)) for line in lines]
        returncode = 0
        exception = ""
    finally:
        if conn is not None:
            conn.commit()
            if use_conn is None:
                conn.close()

    return CompletedTransaction(
        host=host if conn is None else conn.hostname,
        port=port if conn is None else conn.port,
        db=f"{db}" if conn is None else f"{conn.filename}",
        user=user if conn is None else f"{conn.user}",
        access=access.name if conn is None else DBAccess(conn.isolation_level).name,
        returncode=returncode,
        exception=exception,
        query=query,
        params=params,
        time=0 if timer is None else round(timer.interval, 5),
        data=data,
    )


def make_query(procname: str, params: tuple) -> str:
    """Create a query for a stored procedure in a Firebird database.

    Args:
        procname: The name of the stored procedure to execute.
        params: The parameters to pass to the stored procedure.

    Returns:
        query: The query for the stored procedure.
    """
    return f"EXECUTE PROCEDURE {procname} " + ",".join("?" * len(params))


def callproc(
    procname: str,
    params: tuple = (),
    db: Path | str = "",
    host: str = "127.0.0.1",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str = "",
    access: DBAccess = DBAccess.READ_WRITE,
    use_conn: Connection | None = None,
) -> CompletedTransaction:
    """Execute a stored procedure in a Firebird database.

    Args:
        procname: The name of the stored procedure to execute.
        params: The parameters to pass to the stored procedure.
        db: The path or name of the database.
        host: The host address of the server.
        port: The port number of the server.
        user: The username for authentication.
        passwd: The password. If omitted, it is taken from `FIREBIRD_KEY` environment variable.
        access: The access mode for the connection.
        use_conn: An existing connection to use. Takes precedence over the default connection settings.

    Returns:
        result: An named tuple containing the transaction details, including the query result.
    """
    return execute(
        query=make_query(procname, params),
        params=params,
        host=host,
        port=port,
        db=db,
        user=user,
        passwd=passwd,
        use_conn=use_conn,
        access=access,
    )
