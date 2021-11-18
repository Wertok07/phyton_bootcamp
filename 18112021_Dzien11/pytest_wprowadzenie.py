def add(a, b):
    return a + b


print(__name__)
if __name__ == "__main__":
    assert add(3, 5) == 5
    assert add(3, 5) == 7


def sub(a, b):
    return a - b
