from os import getenv
from pathlib import Path

import pytest
from firebirdsql_run import Connection, DBAccess, callproc, connection, execute


@pytest.fixture()
def test_dbh() -> Path:
    return Path("/path/to/test/database.fdb")


@pytest.mark.dbonline()
def test_connection(test_db: Path):
    """Test the connection function."""
    conn = connection(test_db)

    assert isinstance(conn, Connection)
    assert conn.database == f"{test_db}"
    assert conn.host == "127.0.0.1"
    assert conn.port == 3050
    assert conn.user == "TWUSER"
    assert conn.password == ""
    assert conn.isolation_level == DBAccess.READ_WRITE.value


@pytest.mark.dbonline()
def test_execute(test_db: Path):
    result = execute(
        query="SELECT * FROM rdb$database;",
        host="localhost",
        db=test_db,
        user="tests_user",
        passwd=getenv("FIREBIRD_KEY", "tests_password"),
        access=DBAccess.READ_ONLY,
    )

    assert result.host == "localhost"
    assert result.db == f"{test_db}"
    assert result.user == "tests_user"
    assert result.access == DBAccess.READ_ONLY.name
    assert result.returncode == 0
    assert result.exception == ""
    assert result.query == "SELECT * FROM rdb$database;"
    assert result.params == ()
    assert len(result.data) > 0


@pytest.mark.dbonline()
def test_reuse_connection(test_db: Path):
    conn = connection(
        host="localhost",
        db=test_db,
        user="tests_user",
        passwd=getenv("FIREBIRD_KEY", "tests_password"),
        access=DBAccess.READ_ONLY,
    )
    result = execute(
        query="SELECT * FROM rdb$database;",
        use_conn=conn,
    )

    assert isinstance(conn, Connection)
    assert result.host == "localhost"
    assert result.db == f"{test_db}"
    assert result.user == "tests_user"
    assert result.access == DBAccess.READ_ONLY.name
    assert result.returncode == 0
    assert result.exception == ""
    assert result.query == "SELECT * FROM rdb$database;"
    assert result.params == ()
    assert len(result.data) > 0


def test_execute_error():
    result = execute(
        query="SELECT * FROM table;",
        host="localhost",
        db="NONEXISTENT",
        user="NONEXISTENT",
        passwd=getenv("FIREBIRD_KEY", "masterkey"),
        access=DBAccess.READ_ONLY,
    )

    assert result.host == "localhost"
    assert result.db == "NONEXISTENT"
    assert result.user == "NONEXISTENT"
    assert result.access == DBAccess.READ_ONLY.name
    assert result.returncode == 1
    assert len(result.exception) > 0
    assert result.query == "SELECT * FROM table;"
    assert result.params == ()
    assert result.data == []


def test_callproc_error():
    result = callproc(
        procname="PROCNAME",
        params=("p1", "p2", "p3"),
        host="localhost",
        db="NONEXISTENT",
        user="NONEXISTENT",
        passwd=getenv("FIREBIRD_KEY", "masterkey"),
        access=DBAccess.READ_WRITE,
    )

    assert result.host == "localhost"
    assert result.db == "NONEXISTENT"
    assert result.user == "NONEXISTENT"
    assert result.access == DBAccess.READ_WRITE.name
    assert result.returncode == 1
    assert len(result.exception) > 0
    assert result.query == "EXECUTE PROCEDURE PROCNAME ?,?,?"
    assert result.params == ("p1", "p2", "p3")
    assert result.data == []
