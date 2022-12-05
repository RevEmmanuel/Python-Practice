from unittest import TestCase
import chibuzor_assignment


class Test(TestCase):
    def test_largest_of(self):
        self.assertEqual(6, chibuzor_assignment.largest_of([1, 2, 3, 4, 5, 6]))

    def test_reverse_of(self):
        self.assertListEqual([6, 5, 4, 3, 2, 1], chibuzor_assignment.reverse_of([1, 2, 3, 4, 5, 6]))

    def test_occurs_in(self):
        self.assertTrue(chibuzor_assignment.occurs_in(4, [1, 2, 3, 4, 5, 6]))

    def test_occurs_in_fails(self):
        self.assertFalse(chibuzor_assignment.occurs_in(9, [1, 2, 3, 4, 5, 6]))

    def test_odd_elements(self):
        self.assertListEqual([2, 4, 6], chibuzor_assignment.odd_elements([1, 2, 3, 4, 5, 6]))

    def test_even_elements(self):
        self.assertListEqual([1, 3, 5], chibuzor_assignment.even_elements([1, 2, 3, 4, 5, 6]))

    def test_running_total(self):
        self.assertEqual(21, chibuzor_assignment.running_total([1, 2, 3, 4, 5, 6]))

    def test_is_string_palindrome(self):
        self.assertTrue(chibuzor_assignment.is_string_palindrome('Aibohphobia'))

    def test_is_string_palindrome_fails(self):
        self.assertFalse(chibuzor_assignment.is_string_palindrome('Chibuzor'))

    def test_concatenate_two_lists(self):
        list_a = ['a', 'b', 'c']
        list_b = [1, 2, 3]
        self.assertListEqual(['a', 'b', 'c', 1, 2, 3], chibuzor_assignment.concatenate_two_lists(list_a, list_b))

    def test_combine_lists(self):
        names = ["a", "b", "c"]
        array = [1, 2, 3, 4]
        self.assertListEqual(["a", 1, "b", 2, "c", 3, 4], chibuzor_assignment.combine_lists(names, array))

    def test_digits_of(self):
        self.assertListEqual([2, 3, 4, 2], chibuzor_assignment.digits_of(2342))

    def test_swapping(self):
        listed = ['a', 'b']
        self.assertListEqual(['b', 'a'], chibuzor_assignment.swap(listed))

    def test_count_number(self):
        self.assertEqual(7, chibuzor_assignment.count_numbers("A1B2#-+C3D456BG5"))

    def test_to_return_odd(self):
        self.assertEqual(7, chibuzor_assignment.odd_of([2, 4, 6, 7, 8, 10]))

    def test_to_find_missing_number(self):
        self.assertEqual(7, chibuzor_assignment.find_missing_number([1, 2, 3, 4, 5, 6, 8, 9, 10]))

    def test_of_pair_sum(self):
        self.assertEqual([0, 1], chibuzor_assignment.find_index_that_sum_to_target([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], chibuzor_assignment.find_index_that_sum_to_target([3, 2, 4], 6))

    def test_of_uniqueness(self):
        self.assertFalse(chibuzor_assignment.is_unique([1, 2, 2, 3, 6]))
        self.assertTrue(chibuzor_assignment.is_unique([21, 40, 19, 12, 3]))

    def test_of_sum_diagonal(self):
        self.assertEqual(15, chibuzor_assignment.sum_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_of_sum_diagonal_2(self):
        self.assertEqual(5, chibuzor_assignment.sum_diagonal([[1, 2], [3, 4]]))
        self.assertEqual(5, chibuzor_assignment.sum_diagonal([[1, 2], [3, 4]]))

    def test_to_find_first_and_second(self):
        self.assertEqual([90, 87], chibuzor_assignment.first_second([84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84]))
        self.assertEqual([5, 4], chibuzor_assignment.first_second([1, 2, 3, 4, 5, 5]))

    def test_of_search_insert(self):
        nums = [1, 3, 5, 6]
        target = 5
        self.assertEqual(2, chibuzor_assignment.search_insert(nums, target))

        target = 2
        self.assertEqual(1, chibuzor_assignment.search_insert(nums, target))

        target = 7
        self.assertEqual(4, chibuzor_assignment.search_insert(nums, target))

        target = 0
        self.assertEqual(0, chibuzor_assignment.search_insert(nums, target))

        target = 4
        self.assertEqual(2, chibuzor_assignment.search_insert(nums, target))
