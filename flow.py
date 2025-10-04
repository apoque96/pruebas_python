from calculator import sum
from validator import validate
from action import ans

# validate -> sum -> ans
def full_flow(a, b):
    if not validate(a) or not validate(b):
        raise ValueError("Both numbers must be positive")
    result = sum(a, b)
    return ans(result)