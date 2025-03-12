import typer
from src.s8.exercise import app
from typer.testing import CliRunner
import pytest

@pytest.fixture()
def get_runner():
    return CliRunner()

def test_square_success(get_runner):
    result = get_runner.invoke(app, ["square", '5'])
    assert result.exit_code == 0
    assert result.stdout.strip() == "25"

def test_square_failed(get_runner):
    result = get_runner.invoke(app, ["square", '15'])
    assert result.exit_code == 1
    assert "number 15 must be <= 10" in result.stderr

