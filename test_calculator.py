from calculator import *
import pytest

def test_digit_sum():
    assert digit_sum(1) == 1
    assert digit_sum(0) == 0
    assert digit_sum(12) == 3
    with pytest.raises(TypeError):
        digit_sum('aa')

# def test_addition():
#     assert addition(1, 1) == 2
#     assert addition(0, 0) == 0
#     with pytest.raises(TypeError):
#         addition('a', 1)


# def test_substration():
#     assert substraction(1, 0) == 1
#     assert substraction(2, 1) == 1

#     with pytest.raises(TypeError):
#         substraction('a', 1)
