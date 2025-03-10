import pytest

@pytest.fixture
def example():
    return {"name": "PyTest", "version": 6}

def test_name(example):
    assert example["name"] == "PyTest"

def test_version(example):
    assert example["version"] == 6