import unittest
from lab6.Task2.src.main import main


class TestCase(unittest.TestCase):
    def test_with_data_task(self):
        self.assertEqual(main(['add 911 police', 'add 76213 Mom',
                               'add 17239 Bob', 'find 76213', 'find 910',
                               'find 911', 'del 910', 'del 911', 'find 911',
                               'find 76213', 'add 76213 daddy', 'find 76213']),
                         ['Mom', 'not found', 'police', 'not found', 'Mom', 'daddy'])
        self.assertEqual(main(['find 3839442', 'add 123456 me', 'add 0 granny',
                               'find 0', 'find 123456', 'del 0', 'del 0', 'find 0']),
                         ['not found', 'granny', 'me', 'not found'])

    def test_with_other_data(self):
        self.assertEqual(main(['add 100 John', 'add 200 Alice', 'find 100',
                                'find 200', 'del 100', 'find 100', 'del 100', 'find 200']),
                         ['John', 'Alice', 'not found', 'Alice'])
        self.assertEqual(main(['add 300 Mike', 'add 300 Steve', 'find 300']), ['Steve'])
        self.assertEqual(main([]), [])
        self.assertEqual(main(['add 1234 Bill', 'find 1234', 'del 1234', 'find 1234']), ['Bill', 'not found'])
        self.assertEqual(main(['add 111 one', 'add 111 two', 'find 111']), ['two'])


if __name__ == '__main__':
    unittest.main()
