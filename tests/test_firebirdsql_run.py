from pathlib import Path

import pytest
from firebirdsql_run import (
    CompletedTransaction,
    Connection,
    DBAccess,
    callproc,
    connection,
    execute,
)


@pytest.fixture()
def test_db() -> Path:
    return Path("/firebird/data/tests_database.fdb")


@pytest.mark.dbonline()
def test_connection(test_db: Path):
    """Test the connection function."""
    # Variables
    host = "localhost"
    user = "tests_user"
    access = DBAccess.READ_ONLY

    # Execute a query
    # Create a connection object
    conn = connection(
        host=host,
        db=test_db,
        user=user,
        passwd="tests_password",
        access=access,
    )

    assert isinstance(conn, Connection)
    assert conn.filename == f"{test_db}"
    assert conn.hostname == host
    assert conn.port == 3050
    assert conn.user == user
    assert conn.isolation_level == access.value


@pytest.mark.dbonline()
def test_execute(test_db: Path):
    """Test execute function."""
    # Variables
    query = "SELECT * FROM rdb$database;"
    host = "localhost"
    user = "tests_user"
    access = DBAccess.READ_ONLY

    # Execute a query
    result = execute(
        query=query,
        host=host,
        db=test_db,
        user=user,
        passwd="tests_password",
        access=access,
    )

    assert isinstance(result, CompletedTransaction)
    assert result.host == host
    assert result.db == f"{test_db}"
    assert result.user == user
    assert result.access == access.name
    assert result.returncode == 0
    assert result.exception == ""
    assert result.query == query
    assert result.params == ()
    assert len(result.data) > 0


@pytest.mark.dbonline()
def test_execute_with_existing_connection(test_db: Path):
    """Test execute function with an existing connection."""
    # Variables
    query = "SELECT * FROM rdb$database;"
    host = "localhost"
    user = "tests_user"
    access = DBAccess.READ_ONLY

    # Create a connection object
    conn = connection(
        host=host,
        db=test_db,
        user=user,
        passwd="tests_password",
        access=access,
    )
    # Execute a query using the existing connection
    result = execute(query=query, use_conn=conn)
    # Close the connection
    conn.close()

    assert isinstance(conn, Connection)
    assert conn.filename == f"{test_db}"
    assert conn.hostname == host
    assert conn.port == 3050
    assert conn.user == user
    assert conn.isolation_level == access.value
    assert isinstance(result, CompletedTransaction)
    assert result.host == host
    assert result.db == f"{test_db}"
    assert result.user == user
    assert result.access == access.name
    assert result.returncode == 0
    assert result.exception == ""
    assert result.query == query
    assert result.params == ()
    assert len(result.data) > 0


def test_execute_with_exception_with_default_values():
    """Test execute function with default values."""
    # Variables
    query = "SELECT * FROM rdb$database;"

    # Execute a query
    result = execute(query=query)

    assert isinstance(result, CompletedTransaction)
    assert result.returncode == 1
    assert result.exception == "Please setup FIREBIRD_KEY in environment variables."
    assert result.query == query
    assert result.params == ()
    assert isinstance(result.data, list)


def test_execute_with_exception():
    """Test execute function with an exception."""
    # Variables
    query = "SELECT * FROM non_existing_table;"
    host = "localhost"
    db = "NONEXISTENT"
    user = "NONEXISTENT"
    access = DBAccess.READ_ONLY

    # Execute a query
    result = execute(
        query=query,
        host=host,
        db=db,
        user=user,
        passwd="NONEXISTENT",
        access=access,
    )

    assert isinstance(result, CompletedTransaction)
    assert result.host == host
    assert result.db == db
    assert result.user == user
    assert result.access == access.name
    assert result.returncode == 1
    assert len(result.exception) > 0
    assert result.query == query
    assert result.params == ()
    assert result.data == []


def test_callproc_with_exception():
    # Variables
    host = "localhost"
    db = "NONEXISTENT"
    user = "NONEXISTENT"
    access = DBAccess.READ_WRITE

    # Execute a query
    result = callproc(
        procname="PROCNAME",
        params=("p1", "p2", "p3"),
        host=host,
        db=db,
        user=user,
        passwd="NONEXISTENT",
        access=access,
    )

    assert isinstance(result, CompletedTransaction)
    assert result.host == host
    assert result.db == db
    assert result.user == user
    assert result.access == access.name
    assert result.returncode == 1
    assert len(result.exception) > 0
    assert result.query == "EXECUTE PROCEDURE PROCNAME ?,?,?"
    assert result.params == ("p1", "p2", "p3")
    assert result.data == []
