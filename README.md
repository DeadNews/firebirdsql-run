# firebirdsql-run

> [Firebirdsql](https://github.com/nakagami/pyfirebirdsql/) wrapper inspired by [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run)

[![PyPI version](https://img.shields.io/pypi/v/firebirdsql-run)](https://pypi.org/project/firebirdsql-run)
[![CI/CD](https://github.com/DeadNews/firebirdsql-run/actions/workflows/python-app.yml/badge.svg)](https://github.com/DeadNews/firebirdsql-run/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/DeadNews/firebirdsql-run/actions/workflows/python-codeql.yml/badge.svg)](https://github.com/DeadNews/firebirdsql-run/actions/workflows/python-codeql.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DeadNews/firebirdsql-run/main.svg)](https://results.pre-commit.ci/latest/github/DeadNews/firebirdsql-run/main)
[![codecov](https://codecov.io/gh/DeadNews/firebirdsql-run/branch/main/graph/badge.svg?token=OCZDZIYPMC)](https://codecov.io/gh/DeadNews/firebirdsql-run)

## Installation

```sh
pip install firebirdsql-run
```

## Execute

### Table

| maker | model | type |
| ----- | ----- | ---- |
| B     | 1121  | PC   |
| A     | 1232  | PC   |

### Code

```py
result = execute(
    query="SELECT * FROM TABLE",
    host="localhost",
    db="fdb",
    user="sysdba",
    passwd=getenv("FB_PASSWORD"),
)

if result.returncode != 0:
    log.error(result)
else:
    log.info(result)
```

### Success result

```py
CompletedTransaction(
    host="localhost",
    db="fdb",
    user="sysdba",
    returncode=0,
    error="",
    query="SELECT * FROM TABLE",
    params=(),
    data=[
        {"maker": "B", "model": 1121, "type": "PC"},
        {"maker": "A", "model": 1232, "type": "PC"},
    ],
)
```

### Error result

```py
CompletedTransaction(
    host="localhost",
    db="fdb",
    user="sysdba",
    returncode=1,
    error='Dynamic SQL Error\nSQL error code = -204\nTable unknown\nTABLE\nAt line 1, column 15\n',
    query='SELECT * FROM TABLE',
    params=(),
    data=[])
```

## Reuse connection

```py
conn = connection(
    host="localhost",
    db="fdb",
    user="sysdba",
    passwd=getenv("FB_PASSWORD"),
)

execute(use_conn=conn, query="SELECT * FROM TABLE")
...
callproc(use_conn=conn, procname="PROCNAME", params=("p1", "p2", "p3"))
...

conn.close()
```
