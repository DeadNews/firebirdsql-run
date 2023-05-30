#!/usr/bin/env python
from os import environ

import pytest
from firebirdsql_run.util import GetEnvError, get_env


def test_get_env():
    environ["TEST_KEY_1"] = "test"
    assert get_env("TEST_KEY_1") == "test"


def test_get_env_error():
    with pytest.raises(GetEnvError):
        get_env("TEST_KEY_2")
