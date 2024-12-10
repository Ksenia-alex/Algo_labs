from lab4.Task13.src.ClassNode import Node


class Queue:
    """Класс для очереди"""
    def __init__(self, max_size=None):
        self.front = None
        self.rear = None
        self.current_size = 0
        self.max_size = max_size

    def isEmpty(self) -> bool:
        """Проверка на опустошенность"""
        return self.front is None

    def isFull(self) -> bool:
        """Проверка на полноту"""
        if self.max_size is not None:
            return self.current_size > self.max_size
        return False

    def Enqueue(self, data) -> None:
        """Добавление элемента"""
        if self.isFull():
            print("error: queue is full")
            return

        new_node = Node(data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.current_size += 1

    def Dequeue(self):
        """Удаление элемента"""
        if self.isEmpty():
            print("error: queue is empty")
            return

        dequeued_data = self.front.data
        self.front = self.front.next

        if self.isEmpty():
            self.rear = None

        self.current_size -= 1
        return dequeued_data

    def print_queue(self):
        """Печать очереди"""
        current = self.front
        if self.isEmpty():
            print("queue is empty")
            return

        print("elements:")
        while current:
            print(current.data)
            current = current.next
