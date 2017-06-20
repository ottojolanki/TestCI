import unittest
from useless_functions import return_5, raisesValueError, addnums


class TestUselessFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_return_5_equal(self):
        self.assertEqual(return_5(), 5)

    def test_return_5_nequal(self):
        self.assertNotEqual(return_5(), 4)

    def test_raisesValueError(self):
        self.assertRaises(ValueError, raisesValueError)

    def test_addnums(self):
        self.assertEqual(addnums(1, 1), 2)


if __name__ == "__main__":
    unittest.main()
