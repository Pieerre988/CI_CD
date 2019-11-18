import pytest
from calculator import add, multiply
def test_add() : 
	assert add(1, 0) == 1
	assert add(2,-4) == -2


def test_multiply():
    assert multiply(0,1) == 0
    assert multiply(1,2) == 2
    assert multiply(2,3) == 6
    assert multiply(-2,5) == -10
