import pytest
from firebirdsql_run.util import GetEnvError, get_env
from pytest_mock import MockerFixture


def test_get_env_existing_variable(mocker: MockerFixture):
    """Test the get_env function with an existing environment variable."""
    variable = "TEST_VARIABLE"
    value = "test_value"
    mocker.patch.dict("os.environ", {variable: value})

    assert get_env(variable) == value


def test_get_env_non_existing_variable(mocker: MockerFixture):
    """Test the get_env function with a non-existing environment variable."""
    variable = "NON_EXISTING_VARIABLE"
    mocker.patch.dict("os.environ", clear=True)

    with pytest.raises(GetEnvError):
        get_env(variable)
