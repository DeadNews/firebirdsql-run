# firebirdsql-run

> [Firebirdsql](https://github.com/nakagami/pyfirebirdsql/) wrapper inspired by [subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run)

[![PyPI version](https://img.shields.io/pypi/v/firebirdsql-run)](https://pypi.org/project/firebirdsql-run)
[![Documentation](https://img.shields.io/badge/docs-github-blue.svg)](https://deadnews.github.io/firebirdsql-run)
[![Main](https://github.com/DeadNews/firebirdsql-run/actions/workflows/main.yml/badge.svg)](https://github.com/DeadNews/firebirdsql-run/actions/workflows/main.yml)
[![pre-commit.ci](https://results.pre-commit.ci/badge/github/DeadNews/firebirdsql-run/main.svg)](https://results.pre-commit.ci/latest/github/DeadNews/firebirdsql-run/main)
[![codecov](https://codecov.io/gh/DeadNews/firebirdsql-run/branch/main/graph/badge.svg?token=OCZDZIYPMC)](https://codecov.io/gh/DeadNews/firebirdsql-run)

## Table of contents

- [Installation](#installation)
- [Examples](#examples)
- [Env Variables](#env-variables)
- [API Reference](https://deadnews.github.io/firebirdsql-run/reference)

## Installation

```sh
pip install firebirdsql-run
```

## Examples

Execute a query with read-only access:

```py
from firebirdsql_run import DBAccess, execute

# Execute a query with read-only access.
result = execute(query="SELECT * FROM table", db="database", access=DBAccess.READ_ONLY)

# Output: List of dictionaries containing the query results.
print(result.data)
```

Execute a query with parameters and log the result:

```py
# Execute a query with parameters.
result = execute(query="INSERT INTO customers (name, age) VALUES (?, ?)", params=("John", 25))

# Log the result.
if result.returncode != 0:
    logger.error(result)
else:
    logger.info(result)
```

Execute a query using the existing connection:

```py
# Create a connection object.
conn = connection(db="database", access=DBAccess.READ_ONLY)
# Execute a query using the existing connection.
result = execute(query="SELECT * FROM table", use_conn=conn)
# Close the connection.
conn.close()

# Output: Named tuple representing the completed transaction.
print(result)
```

An example of a successful transaction:

```py
>>> print(result)
CompletedTransaction(
    host="127.0.0.1",
    db="database",
    user="TWUSER",
    access="READ_ONLY",
    returncode=0,
    exception="",
    query="SELECT * FROM table",
    params=(),
    time=0.001,
    data=[
        {'id': 1, 'name': 'John Doe', 'department': 'Sales'},
        {'id': 2, 'name': 'Jane Smith', 'department': 'Sales'},
    ],
)
```

An example of a failed transaction:

```py
>>> print(result)
CompletedTransaction(
    host="127.0.0.1",
    db="database",
    user="TWUSER",
    access="READ_ONLY",
    returncode=1,
    exception="Dynamic SQL Error\nSQL error code = -204\nTable unknown\ntable\nAt line 1, column 15\n",
    query="SELECT * FROM table",
    params=(),
    time=0.001,
    data=[],
)
```

## Env Variables

```ini
FIREBIRD_KEY=
```

The `FIREBIRD_KEY` environment variable can be overridden with the functions argument `passwd`.
