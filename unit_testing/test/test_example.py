# test_example.py code
def add(x):
    return x + 1

def add_list(list):
    return sum(list)

def test_add_list():
    assert add_list([1, 2, 3]) == 6, "Result must be 6"

def test_add():
    print("Adding test")
    assert add(3) == 4, "Result must be 4"
