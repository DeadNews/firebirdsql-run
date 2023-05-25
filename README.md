# firebirdsql-run

> [Firebirdsql](https://github.com/nakagami/pyfirebirdsql/) wrapper inspired by [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run)

[![PyPI version](https://img.shields.io/pypi/v/firebirdsql-run)](https://pypi.org/project/firebirdsql-run)
[![Main](https://github.com/DeadNews/firebirdsql-run/actions/workflows/main.yml/badge.svg)](https://github.com/DeadNews/firebirdsql-run/actions/workflows/main.yml)
[![pre-commit.ci](https://results.pre-commit.ci/badge/github/DeadNews/firebirdsql-run/main.svg)](https://results.pre-commit.ci/latest/github/DeadNews/firebirdsql-run/main)
[![codecov](https://codecov.io/gh/DeadNews/firebirdsql-run/branch/main/graph/badge.svg?token=OCZDZIYPMC)](https://codecov.io/gh/DeadNews/firebirdsql-run)

## Installation

```sh
pip install firebirdsql-run
```

## Examples

### Execute

| maker | model | type |
| ----- | ----- | ---- |
| B     | 1121  | PC   |
| A     | 1232  | PC   |

```py
result = execute(
    query="SELECT * FROM TABLE",
    host="localhost",
    db="fdb",
    user="sysdba",
)

if result.returncode != 0:
    log.error(result)
else:
    log.info(result)
```

### Info result example

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

### Error result example

```py
CompletedTransaction(
    host="localhost",
    db="fdb",
    user="sysdba",
    returncode=1,
    error="Dynamic SQL Error\nSQL error code = -204\nTable unknown\nTABLE\nAt line 1, column 15\n",
    query="SELECT * FROM TABLE",
    params=(),
    data=[],
)
```

### Reuse connection

```py
conn = connection(host="localhost", db="fdb", user="sysdba")

execute(use_conn=conn, query="SELECT * FROM TABLE")
...
callproc(use_conn=conn, procname="PROCNAME", params=(...))
...

conn.close()
```

## Env variables

```ini
FIREBIRD_KEY=
```

The `FIREBIRD_KEY` environment variable can be overridden with the optional function argument `passwd`.
