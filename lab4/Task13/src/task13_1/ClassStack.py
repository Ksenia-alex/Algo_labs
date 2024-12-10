from lab4.Task13.src.ClassNode import Node


class Stack:
    """Класс для стека"""
    def __init__(self):
        self.top = None

    def isEmpty(self) -> bool:
        """Проверка на опустошенность"""
        return self.top is None

    def push(self, data) -> None:
        """Добавление элемента"""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Удаление элемента"""
        if self.isEmpty():
            print("error: stack is empty")
            return
        node_pop = self.top
        self.top = self.top.next
        # node_pop.next = None
        return node_pop.data

    def print_stack(self) -> None:
        """Печать стека"""
        current = self.top
        if self.isEmpty():
            print("stack is empty")
            return
        print("elements:")
        while current:
            print(current.data)
            current = current.next
