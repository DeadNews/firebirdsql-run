#!/usr/bin/env python
import pytest

from src.firebirdsql_run import callproc, connection, execute


def test_connection():
    with pytest.raises(ConnectionRefusedError):
        connection(
            host="localhost",
            db="fdb",
            port=3050,
            user="sysdba",
            passwd="masterkey",
        )


def test_execute():
    result = execute(
        query="SELECT * FROM table",
        host="localhost",
        db="fdb",
        user="sysdba",
        passwd="masterkey",
    )

    assert result.host == "localhost"
    assert result.db == "fdb"
    assert result.user == "sysdba"
    assert result.returncode == 1
    assert len(result.error) > 0
    assert result.query == "SELECT * FROM table"
    assert result.params == ()
    assert result.data == []


def test_callproc():
    result = callproc(
        procname="PROCNAME",
        params=("p1", "p2", "p3"),
        host="localhost",
        db="fdb",
        user="sysdba",
        passwd="masterkey",
    )

    assert result.host == "localhost"
    assert result.db == "fdb"
    assert result.user == "sysdba"
    assert result.returncode == 1
    assert len(result.error) > 0
    assert result.query == "EXECUTE PROCEDURE PROCNAME ?,?,?"
    assert result.params == ("p1", "p2", "p3")
    assert result.data == []
