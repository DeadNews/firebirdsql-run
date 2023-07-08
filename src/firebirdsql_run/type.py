#!/usr/bin/env python
"""Types."""
from datetime import datetime
from typing import NamedTuple

FBTypes = str | float | datetime | None
Dataset = list[dict[str, FBTypes]]


class CompletedTransaction(NamedTuple):
    """The return value from execute(), representing a transaction that has finished."""

    host: str
    db: str
    user: str
    returncode: int
    error: str
    query: str
    params: tuple
    data: Dataset


class ExecuteError(Exception):
    """Exception raised for execute transaction errors."""
