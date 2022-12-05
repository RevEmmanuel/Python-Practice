import unittest
from Assignment import print_name
from second_assignment import hypotenuse_of, sum_of_digits, kelvin_of, reverse_list

# def test_something(self):
# self.assertEqual(True, False)  # add assertion here


class MyTestCase(unittest.TestCase):

    def test_printing(self):
        self.assertEqual(print_name("ankie"), "ANKIE")

    def test_return_hypotenuse(self):
        self.assertEqual(hypotenuse_of(3, 4), 5)

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)

    def test_kelvin_of(self):
        self.assertEqual(kelvin_of(6), 279.15)

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3, 4, 5, 5]), [5, 5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
