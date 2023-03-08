import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):

    def test_parameter_not_list_throws_error(self):
        self.assertRaises(TypeError, even_number_of_evens, 5)

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


if __name__ == "__main__":
    unittest.main()
