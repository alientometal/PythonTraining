import unit_testing.fibonacci as fi
import pytest

# Successfull assertion 
@pytest.mark.parametrize(
    "number,expected",
    [
        (3, True),
        (6, False),
        (13, True)
    ]
)
def test_isFibonacci(number, expected):
    assert fi.isFibonacci(number) == expected
    
# Failure assertion
def test_notFibonacci():
    assert fi.isFibonacci(6) == False, "Must be false"

def test_floatFibonacci():
    with pytest.raises(ValueError) as err:
        fi.isFibonacci(3.0)
    assert str(err.value) == "Floats are not supported"
    
def test_stringFibonacci():
    with pytest.raises(TypeError) as err:
        fi.isFibonacci('3')
    assert str(err.value) == "Strings are not supported"

def test_negativesFibonacci():
    with pytest.raises(ValueError) as err:
        fi.isFibonacci(-3)
    assert str(err.value) == "Negatives are not supported"
    
    
def test_FiboSequence(monkeypatch):
    monkeypatch.setattr(fi.FiboNumbers, "get_sequence", lambda x: [1,1,2,3,5])
    Fibo = fi.FiboNumbers()
    assert Fibo.get_sequence() == [1,1,2,3,5]
