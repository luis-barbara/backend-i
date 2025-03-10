from src.s6.sample import add 

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0