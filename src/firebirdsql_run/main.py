#!/usr/bin/env python
"""Firebirdsql wrapper inspired by subprocess.run."""
from pathlib import Path
from socket import getfqdn

from firebirdsql import Connection, connect

from firebirdsql_run.type import CompletedTransaction
from firebirdsql_run.util import get_env


def connection(
    db: Path | str,
    host: str = "localhost",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str | None = None,
) -> Connection:
    """Create a connection to the database."""
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
    host: str = "localhost",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str | None = None,
    use_conn: Connection | None = None,
) -> CompletedTransaction:
    """
    Execute transaction.

    Run the transaction described by args.
    Wait for transaction to complete, then return a CompletedTransaction named tuple.

    An existing connection can be used with `use_conn`, it will not be closed after execution.
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

        conn.commit()
    except Exception as e:  # noqa: BLE001
        data = []
        returncode = 1
        error = f"{e}"
    else:
        data = [dict(zip(columns, line, strict=True)) for line in lines]
        returncode = 0
        error = ""
    finally:
        if conn_success and use_conn is None:
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
    procname: str,
    params: tuple = (),
    db: Path | str = "",
    host: str = "localhost",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str | None = None,
    use_conn: Connection | None = None,
) -> CompletedTransaction:
    """Execute procedure with params."""
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
