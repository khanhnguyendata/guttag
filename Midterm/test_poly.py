import unittest
from poly import general_poly


class TestPoly(unittest.TestCase):
    """
    Test function general_poly
    """

    def test_base_10(self):
        self.assertEqual(general_poly([7, 6, 5, 4])(10), 7654)

    def closure(self):
        closure_function = general_poly([3, 4, 5, 6])
        self.assertEqual(closure_function(10), 3456)

    def test_base_2(self):
        self.assertEqual(general_poly([1, 1, 0, 0, 1, 0])(2), 50)

    def test_empty_coeff(self):
        self.assertEqual(general_poly([])(10), 0)

    def test_zero_coeff(self):
        self.assertEqual(general_poly([0, 0, 0])(10), 0)

    def test_zero_base(self):
        self.assertEqual(general_poly([5, 6, 7])(0), 7)

    def test_zero_coeff_base(self):
        self.assertEqual(general_poly([0, 0, 0])(0), 0)

