from firebirdsql import consts

from firebirdsql_run.type import DBAccess


def test_db_access_read_only():
    """Test the READ_ONLY access mode of DBAccess."""
    assert DBAccess.READ_ONLY == consts.ISOLATION_LEVEL_READ_COMMITED_RO


def test_db_access_read_write():
    """Test the READ_WRITE access mode of DBAccess."""
    assert DBAccess.READ_WRITE == consts.ISOLATION_LEVEL_READ_COMMITED
