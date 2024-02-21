import pytest
from firebirdsql_run.util import GetEnvError, Timer, get_env
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


def test_timer():
    """Test the methods of Timer."""
    with Timer() as t:
        assert isinstance(t, Timer)
        assert hasattr(t, "start")

    assert hasattr(t, "end")
    assert hasattr(t, "interval")
    assert t.start <= t.end


def test_timer_exception():
    """Test the methods of Timer with an exception."""
    with Timer() as t:
        # Simulate an exception
        try:
            msg = "Test exception"
            raise ValueError(msg)  # noqa: TRY301
        except ValueError:
            pass

    assert hasattr(t, "start")
    assert hasattr(t, "end")
    assert hasattr(t, "interval")
    assert t.start <= t.end
    assert t.interval >= 0
