import unittest
from lab4.Task8.src.task8 import postfix_entry


class TestCase(unittest.TestCase):
    def test_an_example_from_the_text(self):
        self.assertEqual(postfix_entry(["8", "9", "+", "1", "7", "-", "*"]), -102)

    def test_with_other_data(self):
        self.assertEqual(postfix_entry(['1', '2', '-']), -1)
        self.assertEqual(postfix_entry(['1', '2', '+']), 3)
        self.assertEqual(postfix_entry(['1', '2', '*']), 2)
        self.assertEqual(postfix_entry(['1', '2', '-', "5", "+", "2", "*"]), 8)


if __name__ == '__main__':
    unittest.main()
