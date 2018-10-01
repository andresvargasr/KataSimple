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

    # Iteration TDD 2
    def test_string_vacioMinimo(self):
        s = Solver();
        result = s.demo("")
        self.assertTrue(result[1] == 0)

    def test_string_un_numeroMinimo(self):
        s = Solver();
        result = s.demo("1")
        self.assertTrue(result[1] == 1)

    def test_string_dos_numerosMinimo(self):
        s = Solver();
        result = s.demo("1, 3")
        self.assertTrue(result[1] == 1)

    def test_string_n_numerosMinimo(self):
        s = Solver();
        result = s.demo("2, 3, 9, 7, 15, 88, 24")
        self.assertTrue(result[1] == 2)

    # Iteration TDD 3

    def test_string_vacioMaximo(self):
        s = Solver();
        result = s.demo("")
        self.assertTrue(result[2] == 0)

    def test_string_un_numeroMaximmo(self):
        s = Solver();
        result = s.demo("1")
        self.assertTrue(result[2] == 1)

    def test_string_dos_numeroMaximmo(self):
        s = Solver();
        result = s.demo("1, 3")
        self.assertTrue(result[2] == 3)

    def test_string_n_numeroMaximmo(self):
        s = Solver();
        result = s.demo("2, 3, 9, 7, 15, 88, 24")
        self.assertTrue(result[2] == 88)

# Iteration TDD 4

    def test_string_vacioPromedio(self):
        s = Solver();
        result = s.demo("")
        self.assertTrue(result[3] == 0)

    def test_string_un_numeroPromedio(self):
        s = Solver();
        result = s.demo("1")
        self.assertTrue(result[3] == 1)

    def test_string_dos_numeroPromedio(self):
        s = Solver();
        result = s.demo("1, 3")
        self.assertTrue(result[3] == 2)

    def test_string_n_numeroPromedio(self):
        s = Solver();
        result = s.demo("2, 3, 9, 10")
        self.assertTrue(result[3] == 6)
