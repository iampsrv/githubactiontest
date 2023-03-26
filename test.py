import pytest
from my_factorial import my_factorial

def test_factorial_1():
    assert my_factorial(0) == 1

def test_factorial_2():
    assert my_factorial(1) == 1

def test_factorial_3():
    assert my_factorial(2) == 2

def test_factorial_4():
    assert my_factorial(5) == 120

def test_factorial_5():
    assert my_factorial(10) == 3628800
