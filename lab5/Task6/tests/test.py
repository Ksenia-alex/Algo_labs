import unittest
from lab5.Task6.src.task6 import process_operations


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(process_operations(8, ['A 3', 'A 4', 'A 2', 'X', 'D 2 1', 'X', 'X', 'X']), ['2', '1', '3', '*'])

    def test_with_other_data(self):
        self.assertEqual(process_operations(3, ['A 3', 'X', 'X']), ['3', '*'])
        self.assertEqual(process_operations(0, []), [])
        self.assertEqual(process_operations(5, ['A 3', 'A 5', 'D 1 4', 'X', 'X']), ['3', '5'])


if __name__ == '__main__':
    unittest.main()
