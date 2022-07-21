#!/usr/bin/env python
from os import environ

from src.firebirdsql_run import getpw


def test_getpw():
    pw = "pbbmaDXpeNKJ7iMS475qnqvCYsymjZ"
    environ["FB_PASSWD"] = pw

    assert getpw() == pw
