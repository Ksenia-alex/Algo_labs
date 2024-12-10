import unittest
from lab4.Task13.src.task13_2.ClassQueue import Queue


class TestCase(unittest.TestCase):
    def test_isEmpty(self):
        self.assertEqual(Queue().isEmpty(), True)
        queue = Queue()
        queue.Enqueue(1)
        self.assertEqual(queue.isEmpty(), False)

    def test_isFull(self):
        queue = Queue(2)
        queue.Enqueue(1)
        queue.Enqueue(2)
        self.assertEqual(queue.isFull(), False)
        queue.Enqueue(3)
        self.assertEqual(queue.isFull(), True)

    def test_Enqueue(self):
        queue = Queue(2)
        queue.Enqueue(1)
        self.assertEqual(queue.print_queue(), None)  # так как функция ничего не возвращает

    def test_Dequeue(self):
        queue = Queue()
        queue.Enqueue(1)
        queue.Enqueue(2)
        queue.Enqueue(3)
        queue.Enqueue(4)
        self.assertEqual(queue.Dequeue(), 1)
        self.assertEqual(queue.Dequeue(), 2)
        self.assertEqual(queue.Dequeue(), 3)
        self.assertEqual(queue.Dequeue(), 4)
        self.assertEqual(queue.Dequeue(), None)


if __name__ == '__main__':
    unittest.main()
