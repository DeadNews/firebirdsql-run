#!/usr/bin/env python
"""Types."""
from datetime import datetime
from typing import NamedTuple

FBTypes = str | float | datetime | None
Dataset = list[dict[str, FBTypes]]


class CompletedTransaction(NamedTuple):
    """
    Represents a completed transaction in a database.

    Attributes:
        host (str): The host where the transaction was executed.
        db (str): The database where the transaction was executed.
        user (str): The user who executed the transaction.
        returncode (int): The return code of the transaction execution.
        error (str): The error message, if any, encountered during the transaction execution.
        query (str): The SQL query executed in the transaction.
        params (tuple): The parameters used in the SQL query.
        data (Dataset): The data returned by the transaction, represented as a list of dictionaries.
    """

    host: str
    db: str
    user: str
    returncode: int
    error: str
    query: str
    params: tuple
    data: Dataset


class ExecuteError(Exception):
    """Exception raised when an error occurs during the transaction execution."""
