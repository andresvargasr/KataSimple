from unittest import TestCase
from Solver import Solver


class TestSolver(TestCase):

    # Iteration TDD 1
    def test_string_vacio(self):
        s = Solver();
        result = s.demo("")
        self.assertTrue(result[0] == 0)

    def test_string_un_numero(self):
        s = Solver();
        result = s.demo("1")
        self.assertTrue(result[0] == 1)

    def test_string_dos_numeros(self):
        s = Solver();
        result = s.demo("1, 3")
        self.assertTrue(result[0] == 2)

    def test_string_n_numeros(self):
        s = Solver();
        result = s.demo("1, 3, 9, 7, 1, 88, 24")
        self.assertTrue(result[0] == 7)

