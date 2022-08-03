#!/usr/bin/env python3
"""
Firebirdsql wrapper inspired by subprocess.run
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from socket import getfqdn
from typing import NamedTuple, Union

from firebirdsql import Connection, connect

FBTypes = Union[str, float, datetime, None]
Dataset = list[dict[str, FBTypes]]


class CompletedTransaction(NamedTuple):
    """
    The return value from execute(), representing a transaction that has finished.
    """

    host: str
    db: str
    user: str
    returncode: int
    error: str
    query: str
    params: tuple
    data: Dataset


def connection(
    db: Path | str,
    host: str = "localhost",
    port: int = 3050,
    user: str = "TWUSER",
    passwd: str | None = None,
) -> Connection:
    """
    Creating a connection to the database.
    """
    return connect(
        host=getfqdn(host),
        database=f"{db}",
        port=port,
        user=user,
        password=passwd,
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

        if use_conn is None:
            conn.close()
    except Exception as e:
        data = []
        returncode = 1
        error = f"{e}"
    else:
        data = [dict(zip(columns, line)) for line in lines]
        returncode = 0
        error = ""

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
    """
    Execute procedure with params.
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
