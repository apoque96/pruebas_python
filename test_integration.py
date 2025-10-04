from calculator import sum
from validator import validate
from action import ans

def test_sum_and_validate():
    # Valid sum
    assert validate(4) and validate(6)
    assert sum(4, 6) == 10

def test_validate_and_ans():
    num = 7
    if validate(num):
        assert "7" in ans(num)