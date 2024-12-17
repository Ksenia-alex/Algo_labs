import unittest
from lab6.Task1.src.task1 import Set


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(Set(['A 2', 'A 5', 'A 3', '? 2', '? 4', 'A 2', 'D 2', '? 2']), ["Y", "N", "N"])

    def test_with_other_data(self):
        self.assertEqual(Set([]), [])
        self.assertEqual(Set(['A 2', 'A 5', 'A 3', 'A 2', 'D 2']), [])
        self.assertEqual(Set(['A 5', 'A 3', '? 2', '? 4', 'A 2', 'D 2', '? 2']), ["N", "N", "N"])
        self.assertEqual(Set(['A 2', 'D 2', 'A 4', '? 2', '? 4', 'A 2', '? 2']), ["N", "Y", "Y"])
        self.assertEqual(Set(['? 2', '? 4', 'A 2', 'D 2', '? 2']), ["N", "N", "N"])
        self.assertEqual(Set(['A 2', 'A 5', 'A 3', 'A 2', 'D 2', '? 2']), ["N"])


if __name__ == '__main__':
    unittest.main()
