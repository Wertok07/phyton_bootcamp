import unittest
from pytest_wprowadzenie import add
from pytest_wprowadzenie import sub


# unittest
class testAdd(unittest.TestCase):

    def test_add_two_positive_numbers(self):
        result = add(1, 3)
        self.assertEqual(result, 4)


# pytest
def test_add_two_negative_numbers():
    assert add(-1, -1) == -2


def test_sub_two_positive_number():
    assert sub(1, 2) == -1
    assert sub(2, 14) == -12
