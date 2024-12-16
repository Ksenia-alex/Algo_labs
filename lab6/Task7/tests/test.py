import unittest
from lab6.Task7.src.task7 import count_beautiful_pairs


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        result = count_beautiful_pairs(7, 'abacaba', [('a', 'a')])
        self.assertEqual(result, 6)
        result = count_beautiful_pairs(7, 'abacaba', [('a', 'b'), ('a', 'c'), ('b', 'b')])
        self.assertEqual(result, 7)

    def test_with_other_data(self):
        result = count_beautiful_pairs(7, "abacaba", [("a", "a")])
        self.assertEqual(result, 6)
        result = count_beautiful_pairs(5, "abcde", [("z", "y")])
        self.assertEqual(result, 0)
        result = count_beautiful_pairs(0, "", [("a", "b")])
        self.assertEqual(result, 0)
        result = count_beautiful_pairs(4, "aaaa", [("a", "a")])
        self.assertEqual(result, 6)
        result = count_beautiful_pairs(3, "xyz", [("a", "b"), ("c", "d"), ("e", "f")])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
