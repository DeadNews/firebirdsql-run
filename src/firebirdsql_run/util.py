#!/usr/bin/env python
"""Utils."""
from os import getenv


class GetEnvError(Exception):
    """Exception raised for getenv errors."""


def get_env(key: str) -> str:
    """Get environment variable or raise an error."""
    if value := getenv(key):
        return value

    msg = f"Please setup {key} in environment variables."
    raise GetEnvError(msg)
