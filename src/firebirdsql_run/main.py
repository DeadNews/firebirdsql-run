#!/usr/bin/env python
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
    db: Path | str,
    query: str,
    params: tuple = (),
    host: str = "127.0.0.1",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str = "",
    use_conn: Connection | None = None,
) -> CompletedTransaction:
    """
    Execute a transaction in a Firebird database.

    Args:
        db (Path | str): The path to the Firebird database file.
        query (str): The SQL query to be executed.
        params (tuple, optional): Optional parameters to be used in the query. Defaults to ().
        host (str, optional): The host address of the Firebird server. Defaults to "127.0.0.1".
        port (int, optional): The port number of the Firebird server. Defaults to 3050.
        user (str, optional): The username for authentication. Defaults to "TWUSER".
        passwd (str, optional): The password for authentication.
            If not provided, it retrieves the password from the FIREBIRD_KEY environment variable.
        use_conn (Connection | None, optional): The existing connection to be used for the transaction.

    Returns:
        CompletedTransaction: A named tuple containing information about the executed transaction.
    """
    conn_success = False
    try:
        conn = (
            connection(host=host, db=db, port=port, user=user, passwd=passwd)
            if use_conn is None
            else use_conn
        )
        conn_success = True

        cur = conn.cursor()
        cur.execute(query=query, params=params)

        lines = cur.fetchall()
        columns = [f"{col[0]}".lower() for col in cur.description]
    except Exception as e:  # noqa: BLE001
        data = []
        returncode = 1
        error = f"{e}"
    else:
        data = [dict(zip(columns, line, strict=True)) for line in lines]
        returncode = 0
        error = ""
    finally:
        if conn_success:
            conn.commit()
            if use_conn is None:
                conn.close()

    return CompletedTransaction(
        host=conn.hostname if conn_success else host,
        db=conn.filename if conn_success else db,
        user=conn.user if conn_success else user,
        returncode=returncode,
        error=error,
        query=query,
        params=params,
        data=data,
    )


def callproc(
    db: Path | str,
    procname: str,
    params: tuple = (),
    host: str = "127.0.0.1",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str = "",
    use_conn: Connection | None = None,
) -> CompletedTransaction:
    """
    Execute a stored procedure in a Firebird database.

    Args:
        db (Path | str): The path to the Firebird database file.
        procname (str): The name of the stored procedure to be executed.
        params (tuple, optional): Optional parameters to be passed to the stored procedure. Defaults to ().
        host (str, optional): The host address of the Firebird server. Defaults to "127.0.0.1".
        port (int, optional): The port number of the Firebird server. Defaults to 3050.
        user (str, optional): The username for authentication. Defaults to "TWUSER".
        passwd (str, optional): The password for authentication.
            If not provided, it retrieves the password from the FIREBIRD_KEY environment variable.
        use_conn (Connection | None, optional): The existing connection to be used for the transaction.

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
