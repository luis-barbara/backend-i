from src.s8.exercise import app
from typer.testing import CliRunner
import pytest

@pytest.fixture()
def get_runner():
    return CliRunner()

def test_square(get_runner):
    result = get_runner.invoke(app, ["square", "5"])
    print("STDOUT:", result.stdout) 
    print("STDERR:", result.stderr) 
    assert result.exit_code == 0
    assert "25" in result.stdout



