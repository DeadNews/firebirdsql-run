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


@pytest.mark.docker()
def test_execute():
    result = execute(
        # query="SELECT * FROM rdb$database;",
        query="SELECT rdb$relation_name FROM rdb$relations WHERE rdb$view_blr IS NULL AND (rdb$system_flag IS NULL OR rdb$system_flag = 0);",
        host="localhost",
        db="/firebird/data/test.fdb",
        user="user",
        passwd=getenv("FB_PASSWORD", "password"),
    )

    assert result.host == "localhost"
    assert result.db == "/firebird/data/test.fdb"
    assert result.user == "user"
    assert result.returncode == 0
    assert result.error == ""
    # assert result.query == "SELECT * FROM rdb$database;"
    assert (
        result.query
        == "SELECT rdb$relation_name FROM rdb$relations WHERE rdb$view_blr IS NULL AND (rdb$system_flag IS NULL OR rdb$system_flag = 0);"
    )
    assert result.params == ()
    assert result.data == [
        {
            "rdb$character_set_name": "UTF8",
            "rdb$description": None,
            "rdb$relation_id": 128,
            "rdb$security_class": None,
        }
    ]


def test_execute_error():
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
    assert result.query == "SELECT * FROM table;"
    assert result.params == ()
    assert result.data == []


def test_callproc_error():
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
