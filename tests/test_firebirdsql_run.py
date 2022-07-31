#!/usr/bin/env python
from os import getenv
from socket import gaierror

import pytest

from src.firebirdsql_run import callproc, connection, execute


def test_connection():
    with pytest.raises(gaierror):
        connection(
            host="random",
            db="fdb",
            port=3050,
            user="sysdba",
            passwd=getenv("FB_PASSWORD", "masterkey"),
        )


def test_execute_fail():
    result = execute(
        query="SELECT * FROM table;",
        host="random",
        db="fdb",
        user="sysdba",
        passwd=getenv("FB_PASSWORD", "masterkey"),
    )

    assert result.host == "random"
    assert result.db == "fdb"
    assert result.user == "sysdba"
    assert result.returncode == 1
    assert len(result.error) > 0
    assert result.query == "SELECT * FROM table"
    assert result.params == ()
    assert result.data == []


def test_execute():
    result = execute(
        query="SELECT * FROM rdb$database;",
        host="localhost",
        db="/firebird/data/my_database.fdb",
        user="my_user",
        passwd=getenv("FB_PASSWORD", "my_password"),
    )

    assert result.returncode == 0


def test_callproc_fail():
    result = callproc(
        procname="PROCNAME",
        params=("p1", "p2", "p3"),
        host="random",
        db="fdb",
        user="sysdba",
        passwd=getenv("FB_PASSWORD", "masterkey"),
    )

    assert result.host == "random"
    assert result.db == "fdb"
    assert result.user == "sysdba"
    assert result.returncode == 1
    assert len(result.error) > 0
    assert result.query == "EXECUTE PROCEDURE PROCNAME ?,?,?"
    assert result.params == ("p1", "p2", "p3")
    assert result.data == []
