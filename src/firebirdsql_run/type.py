"""Type definitions for the package."""

from datetime import datetime
from enum import IntEnum
from typing import NamedTuple

from firebirdsql import consts

FBTypes = str | float | datetime | None
Dataset = list[dict[str, FBTypes]]


class DBAccess(IntEnum):
    """Enumeration of access modes for FirebirdSQL connections."""

    READ_ONLY = consts.ISOLATION_LEVEL_READ_COMMITED_RO
    READ_WRITE = consts.ISOLATION_LEVEL_READ_COMMITED


class CompletedTransaction(NamedTuple):
    """Represents a completed transaction in a database.

    Attributes:
        host (str): The host address of the server.
        port (int): The port number of the server.
        db (str): The database where the transaction was executed.
        user (str): The user who executed the transaction.
        access (str): The access mode used for the transaction.
        returncode (int): The return code of the transaction execution.
        exception (str): The exception message if the transaction failed.
        query (str): The SQL query executed in the transaction.
        params (tuple): The parameters used in the SQL query.
        data (Dataset): The data returned by the transaction, represented as a list of dictionaries.
    """

    host: str
    db: str
    port: int
    user: str
    access: str
    returncode: int
    exception: str
    query: str
    params: tuple
    data: Dataset


class ExecuteError(Exception):
    """Exception raised when an error occurs during the transaction execution."""
