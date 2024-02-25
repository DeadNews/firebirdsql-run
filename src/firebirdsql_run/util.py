"""Utility functions for the package."""

import time
from os import getenv
from types import TracebackType


class GetEnvError(Exception):
    """Exception raised when an environment variable is not found."""


def get_env(variable: str) -> str:
    """Get the value of an environment variable.

    Args:
        variable: The name of the environment variable to retrieve.

    Returns:
        value: The value of the environment variable, if found.

    Raises:
        GetEnvError: If the environment variable is not found.
    """
    if value := getenv(variable):
        return value

    msg = f"Please setup {variable} in environment variables."
    raise GetEnvError(msg)


class Timer:
    """A context manager for measuring the execution time of a code block."""

    def __enter__(self: "Timer") -> "Timer":
        """Enter the context and start the timer."""
        self.start = time.perf_counter()
        return self

    def __exit__(
        self: "Timer",
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Exit the context and calculate the elapsed time."""
        self.end = time.perf_counter()
        self.interval = self.end - self.start
