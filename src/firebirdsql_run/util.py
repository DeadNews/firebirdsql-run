#!/usr/bin/env python
"""Utils."""
from os import getenv


class GetEnvError(Exception):
    """Exception raised when an environment variable is not found."""


def get_env(variable: str) -> str:
    """
    Get the value of an environment variable.

    Args:
        variable (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the environment variable, if found.

    Raises:
        GetEnvError: If the environment variable is not found.
    """
    if value := getenv(variable):
        return value

    msg = f"Please setup {variable} in environment variables."
    raise GetEnvError(msg)
