import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.calculator import Calculator

def test_add():
  calculator = Calculator(1, 2)
  assert calculator.add() == 3

def test_subtract():
  calculator = Calculator(1, 2)
  assert calculator.subtract() == -1

def test_multiply():
  calculator = Calculator(1, 2)
  assert calculator.multiply() == 2

def test_divide():
  calculator = Calculator(2, 2)
  assert calculator.divide() == 1

def test_power():
  calculator = Calculator(1, 2)
  assert calculator.power() == 1

def test_square():
  calculator = Calculator(1, 2)
  assert calculator.square() == 1

def test_cube():
  calculator = Calculator(1, 2)
  assert calculator.cube() == 1