import unittest
from lab4.Task2.src.task2 import algo_queue


class QueueTestCase(unittest.TestCase):

    def test_an_example_from_the_text(self):
        commands = ["+ 1", "+ 10", "-", "-"]
        self.assertEqual(algo_queue(commands), ["1", "10"])

    def test_with_other_data(self):
        commands = ["+ 10", "+ 10", "-", "+ -23", "+ 194", "-", "-"]
        self.assertEqual(algo_queue(commands), ["10", "10", "-23"])

        commands = ["+ -1000000000", "+ 1000000000", "-", "-"]
        self.assertEqual(algo_queue(commands), ["-1000000000", "1000000000"])

        commands = ["+ 9", "+ 144", "-", "+ 2111", "+ 282", "-", "-"]
        self.assertEqual(algo_queue(commands), ["9", "144", "2111"])

        commands = ["+ 1", "+ 2", "+ 3"]
        self.assertEqual(algo_queue(commands), [])