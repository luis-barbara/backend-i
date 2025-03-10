from src.s6.challenge import factorial
import pytest

def test_factorial():
    with pytest.raises(ValueError, match="O factorial não pode ser negativo"):
        factorial(-1)  


