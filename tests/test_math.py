"""
Testing for the math.py module.
"""

import friendly_computing_machine as fcm
import pytest

def test_add():
    """
    
    """
    assert fcm.math.add (5, 2) == 7
    assert fcm.math.add (2, 5) == 7
testdata = [
    (2, 5, 10),
    (1, 2, 2),
    (11, 9, 99),
    (11, 0, 0),
    (0, 0, 0)
]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_mult(a, b, expected):
    """

    """
    assert fcm.math.mult(a, b) == expected
    assert fcm.math.mult(b, a) == expected

def test_division():
    """

    """
    assert fcm.math.division(5, 2) == 2.5
    assert fcm.math.division(2, 1) == 2

def test_exp():
    """

    """
    assert fcm.math.exp(3, 2) == 9
    assert fcm.math.exp(2, 1) == 2 
