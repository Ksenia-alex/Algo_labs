import unittest
from lab4.Task13.src.task13_1.ClassStack import Stack


class TestCase(unittest.TestCase):
    def test_isEmpty(self):
        self.assertEqual(Stack().isEmpty(), True)
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.isEmpty(), False)

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.print_stack(), None)  # так как функция ничего не возвращает

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), None)


if __name__ == '__main__':
    unittest.main()
