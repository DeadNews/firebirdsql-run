#!/usr/bin/env python
from os import getenv
from socket import gaierror

import pytest
from firebirdsql_run import callproc, connection, execute


def test_connection_error():
    with pytest.raises(gaierror):
        connection(
            host="random",
            db="fdb",
            port=3050,
            user="sysdba",
            passwd=getenv("FIREBIRD_KEY", "masterkey"),
        )


@pytest.mark.docker()
def test_execute():
    result = execute(
        query="SELECT * FROM rdb$database;",
        host="localhost",
        db="/firebird/data/my_database.fdb",
        user="my_user",
        passwd=getenv("FIREBIRD_KEY", "my_password"),
    )

    assert result.host == "localhost"
    assert result.db == "/firebird/data/my_database.fdb"
    assert result.user == "my_user"
    assert result.returncode == 0
    assert result.error == ""
    assert result.query == "SELECT * FROM rdb$database;"
    assert result.params == ()
    assert len(result.data) > 0


@pytest.mark.docker()
def test_reuse_connection():
    conn = connection(
        host="localhost",
        db="/firebird/data/my_database.fdb",
        user="my_user",
        passwd=getenv("FIREBIRD_KEY", "my_password"),
    )
    result = execute(
        query="SELECT * FROM rdb$database;",
        use_conn=conn,
    )

    assert result.host == "localhost"
    assert result.db == "/firebird/data/my_database.fdb"
    assert result.user == "my_user"
    assert result.returncode == 0
    assert result.error == ""
    assert result.query == "SELECT * FROM rdb$database;"
    assert result.params == ()
    assert len(result.data) > 0


def test_execute_error():
    result = execute(
        query="SELECT * FROM table;",
        host="random",
        db="fdb",
        user="sysdba",
        passwd=getenv("FIREBIRD_KEY", "masterkey"),
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
        passwd=getenv("FIREBIRD_KEY", "masterkey"),
    )

    assert result.host == "random"
    assert result.db == "fdb"
    assert result.user == "sysdba"
    assert result.returncode == 1
    assert len(result.error) > 0
    assert result.query == "EXECUTE PROCEDURE PROCNAME ?,?,?"
    assert result.params == ("p1", "p2", "p3")
    assert result.data == []
