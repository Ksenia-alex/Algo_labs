import unittest
from lab4.Task9.src.task9 import queue_polyclinic


class TestCase(unittest.TestCase):
    def test_with_data_text(self):
        self.assertEqual(queue_polyclinic(["+ 1", "+ 2", "-", "+ 3", "+ 4", "-", "-"]),
                         ["1", "2", "3"])

        self.assertEqual(queue_polyclinic(["+ 1", "+ 2", "* 3", "-", "+ 4", "* 5", "-", "-", "-", "-"]),
                         ["1", "3", "2", "5", "4"])

    def test_with_other_data(self):
        self.assertEqual(queue_polyclinic(["+ 1", "+ 2", "-", "+ 3", "+ 4", "-", "-","+ 5", "+ 6", "-", "+ 7", "+ 8", "-", "-"]),
                         ["1", "2", "3", "4", "5", "6"])

        self.assertEqual(queue_polyclinic(["+ 1", "+ 2", "* 3", "-", "+ 4", "* 5", "-", "-", "-", "-",
                                           "+ 6", "+ 7", "* 8", "-", "+ 10", "* 11", "-", "-", "-", "-"]),
                         ["1", "3", "2", "5", "4", "6", "8", "7", "11", "10"])


if __name__ == '__main__':
    unittest.main()
