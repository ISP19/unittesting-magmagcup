import unittest
from listutil import unique


class UniqueTest(unittest.TestCase):
    """Test the methods and constructor of the function unique. """
    def test_empty_list(self):
        """
        Test function with empty list
        'Borderline cases'
        :return: empty list
        """
        self.assertEqual([], unique([]))

    def test_single_item_list(self):
        """
        Test function unique with only 1 item in list.
        'Borderline cases'
        :return: list with 1 item.
        """
        self.assertListEqual(['hi'], unique(['hi']))
        self.assertListEqual([5], unique([5]))

    def test_one_item_many_times(self):
        '''
        Test function unique with same multiple item in list.
        'typical cases'
        :return: list with 1 item
        '''
        self.assertListEqual(['a'], unique(['a', 'a', 'a']))
        self.assertListEqual([5], unique([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        self.assertListEqual([[1, 2, 3]], unique([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

    def test_many_item_many_times_many_orders(self):
        """
        Test function with many item, many times ,many orders
        'typical cases'
        :return:
        """
        lst = [1, 2, 2, 4, [1, 2, 3], 1, [1, 2, 2, 3], [1, 2, 3]]
        self.assertListEqual([1, 2, 4, [1, 2, 3], [1, 2, 2, 3]], unique(lst))
        lst = [1, 2, {'fruit': 'Banana'}, 3, 4, 5, 6, 4, True, {'fruit': 'Banana'}, 3, True, 2, 1, False, {'fruit': 'Banana'}, 5, 6, 3, 4]
        self.assertListEqual([1, 2, {'fruit': 'Banana'}, 3, 4, 5, 6, True], unique(lst))

    def test_argument_not_a_list(self):
        """
        Use another type of input
        'Impossible case'
        :return:
        """
        with self.assertRaises(TypeError):
            unique(5)
        with self.assertRaises(TypeError):
            unique('w')

    def test_large_list(self):
        """
        humongous list
        'Extreme case'
        :return:
        """
        humongous_list = [num for num in range(0, 1000)]
        self.assertEqual(humongous_list, unique(humongous_list))


if __name__ == '__main__':
    unittest.main()