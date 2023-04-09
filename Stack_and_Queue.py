class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """добавляет новый элемент на вершину стека"""
        self.items.append(item)

    def pop(self):
        """удаляет и возвращает элемент, находящийся на вершине стека"""
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.items.pop()

    def peek(self):
        """возвращает элемент, находящийся на вершине стека, но не удаляет его"""
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.items[-1]

    def is_empty(self):
        """возвращает True, если стек пустой, и False в противном случае"""
        return len(self.items) == 0

    def size(self):
        """возвращает количество элементов в стеке"""
        return len(self.items)


class Queue:
    def __init__(self):
        self.queue_items = []

    def enqueue(self, item):
        self.queue_items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue_items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue_items[0]

    def is_empty(self):
        return len(self.queue_items) == 0

    def size(self):
        return len(self.queue_items)

