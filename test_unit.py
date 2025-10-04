from calculator import sum
from validator import validate
from action import ans

def test_sum():
    assert sum(2, 3) == 5
    assert sum(1, 8) == 9

def test_validate():
    assert validate(8)
    assert not validate(-1)

def test_ans():
    assert "5" in ans(5)
    assert "9" in ans(9)