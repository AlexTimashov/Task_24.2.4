import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 6) == 30

    def test_division_success(self):
        assert self.calc.division(self, 90, 30) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 7) != 2

    def test_adding_success(self):
        assert self.calc.adding(self, 6, 8) == 14

    def teardown(self):
        print("Выполнение метода Teardown")
