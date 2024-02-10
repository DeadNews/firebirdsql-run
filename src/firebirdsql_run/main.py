"""Firebirdsql wrapper inspired by subprocess.run."""
from pathlib import Path
from socket import getfqdn

from firebirdsql import Connection, connect

from firebirdsql_run.type import CompletedTransaction
from firebirdsql_run.util import get_env


def connection(
    db: Path | str,
    host: str = "127.0.0.1",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str = "",
) -> Connection:
    """
    Create a connection to a Firebird database using the firebirdsql library.

    Args:
        db (Path | str): The path to the Firebird database file.
        host (str, optional): The host address of the Firebird server. Defaults to "127.0.0.1".
        port (int, optional): The port number of the Firebird server. Defaults to 3050.
        user (str, optional): The username for authentication. Defaults to "TWUSER".
        passwd (str, optional): The password for authentication.
            If not provided, it retrieves the password from the FIREBIRD_KEY environment variable.

    Returns:
        Connection: A Connection object representing the connection to the Firebird database.
    """
    return connect(
        host=getfqdn(host),
        database=f"{db}",
        port=port,
        user=user,
        password=passwd or get_env("FIREBIRD_KEY"),
    )


def execute(
    query: str,
    params: tuple = (),
    db: Path | str = "",
    host: str = "127.0.0.1",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str = "",
    use_conn: Connection | None = None,
) -> CompletedTransaction:
    """
    Execute a transaction in a Firebird database.

    Args:
        query (str): The SQL query to be executed.
        params (tuple, optional): Optional parameters to be used in the query. Defaults to ().
        db (Path | str, optional): The path to the Firebird database file. Defaults to "".
        host (str, optional): The host address of the Firebird server. Defaults to "127.0.0.1".
        port (int, optional): The port number of the Firebird server. Defaults to 3050.
        user (str, optional): The username for authentication. Defaults to "TWUSER".
        passwd (str, optional): The password for authentication.
            If not provided, it retrieves the password from the FIREBIRD_KEY environment variable.
        use_conn (Connection | None, optional): The existing connection to be used for the transaction.
            Takes precedence over the default connection settings.

    Returns:
        CompletedTransaction: A named tuple containing information about the executed transaction.
    """
    conn: Connection | None = None
    try:
        conn = (
            connection(host=host, db=db, port=port, user=user, passwd=passwd)
            if use_conn is None
            else use_conn
        )
        cur = conn.cursor()
        cur.execute(query=query, params=params)

        lines = cur.fetchall()
        descr = cur.description
    except Exception as e:  # noqa: BLE001
        data = []
        returncode = 1
        error = f"{e}"
    else:
        columns = [] if descr is None else [f"{col[0]}".lower() for col in descr]
        data = [] if lines is None else [dict(zip(columns, line, strict=True)) for line in lines]
        returncode = 0
        error = ""
    finally:
        if conn is not None:
            conn.commit()
            if use_conn is None:
                conn.close()

    return CompletedTransaction(
        host=host if conn is None else conn.hostname,
        db=f"{db}" if conn is None else f"{conn.filename}",
        user=user if conn is None else f"{conn.user}",
        returncode=returncode,
        error=error,
        query=query,
        params=params,
        data=data,
    )


def callproc(
    procname: str,
    params: tuple = (),
    db: Path | str = "",
    host: str = "127.0.0.1",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str = "",
    use_conn: Connection | None = None,
) -> CompletedTransaction:
    """
    Execute a stored procedure in a Firebird database.

    Args:
        procname (str): The name of the stored procedure to be executed.
        params (tuple, optional): Optional parameters to be passed to the stored procedure. Defaults to ().
        db (Path | str, optional): The path to the Firebird database file. Defaults to "".
        host (str, optional): The host address of the Firebird server. Defaults to "127.0.0.1".
        port (int, optional): The port number of the Firebird server. Defaults to 3050.
        user (str, optional): The username for authentication. Defaults to "TWUSER".
        passwd (str, optional): The password for authentication.
            If not provided, it retrieves the password from the FIREBIRD_KEY environment variable.
        use_conn (Connection | None, optional): The existing connection to be used for the transaction.
            Takes precedence over the default connection settings.

    Returns:
        CompletedTransaction: A named tuple containing information about the executed transaction.
    """
    query = f"EXECUTE PROCEDURE {procname} " + ",".join("?" * len(params))

    return execute(
        query=query,
        params=params,
        host=host,
        port=port,
        db=db,
        user=user,
        passwd=passwd,
        use_conn=use_conn,
    )
