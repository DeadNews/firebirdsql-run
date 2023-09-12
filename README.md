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

- Execute a transaction

```py
result = execute(query="SELECT * FROM table", db="database")
print(result.data)  # Output: List of dictionaries containing the query results
```

- Execute a transaction with custom parameters and an existing connection

```py
conn = connection(db="/path/to/database.fdb")
result = execute("INSERT INTO customers (name, age) VALUES (?, ?)", params=("John", 25), use_conn=conn)
print(result.returncode)  # Output: 0 (success)
conn.close()
```

## Representation of a completed transaction

- Table

| maker | model | type |
| ----- | ----- | ---- |
| B     | 1121  | PC   |
| A     | 1232  | PC   |

- Success example

```py
CompletedTransaction(
    host="127.0.0.1",
    db="database",
    user="TWUSER",
    returncode=0,
    error="",
    query="SELECT * FROM table",
    params=(),
    data=[
        {"maker": "B", "model": 1121, "type": "PC"},
        {"maker": "A", "model": 1232, "type": "PC"},
    ],
)
```

- Error example

```py
CompletedTransaction(
    host="127.0.0.1",
    db="database",
    user="TWUSER",
    returncode=1,
    error="Dynamic SQL Error\nSQL error code = -204\nTable unknown\ntable\nAt line 1, column 15\n",
    query="SELECT * FROM table",
    params=(),
    data=[],
)
```

## Env variables

```ini
FIREBIRD_KEY=
```

The `FIREBIRD_KEY` environment variable can be overridden with the function argument `passwd`.
