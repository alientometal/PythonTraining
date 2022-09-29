# test_example_division.py code
import pytest
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0
        
def test_recursion_depth():
    with pytest.raises(RecursionError) as excinfo:
        def f():
            f()
        f()
    assert 'maxima recursión' in str(excinfo.value)
    
def divide(number_one, number_two):
    if number_two == 0:
        raise ValueError('Cannot be divided with this value')
    return number_one / number_two
 
def test_zero_division():
    with pytest.raises(ValueError) as e:
        divide(1, 0)
    assert str(e.value) == 'Cannot be divided with this value' 
