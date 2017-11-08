import unittest
from ordered_keys_with_value import keysWithValue


class TestOrderedKeys(unittest.TestCase):
    """
    Unit test keysWithValue function
    """
    def test_normal_dict(self):
        d1 = {1: 3, 2: 4, 5: 3, 4: 2}
        self.assertEqual(keysWithValue(d1, 3), [1, 5])
        self.assertEqual(keysWithValue(d1, 2), [4])
        self.assertEqual(keysWithValue(d1, 4), [2])

    def test_empty_dict(self):
        self.assertEqual(keysWithValue({}, 2), [])

    def test_dict_without_value(self):
        d2 = {1: 2, 3: 4}
        self.assertEqual(keysWithValue(d2, 9), [])
