#!coding=utf8


class Queue:
    class Node:
        def __init__(self, value):
            self.next = None
            self.value = value

    class EmptyError(Exception):
        pass

    def __init__(self, *args):
        self.first = None
        self.last = None
        self.size = 0

        if args:
            for value in args:
                self.enqueue(value)

    def enqueue(self, value):
        if not self.first:
            self.first = self.Node(value)
            self.last = self.first

        else:
            self.last.next = self.Node(value)
            self.last = self.last.next

        self.size += 1

    def pop(self):
        if not self.first:
            raise self.EmptyError

        value = self.first.value
        self.first = self.first.next

        self.size -= 1
        return value

    def top(self):
        if not self.first:
            raise self.EmptyError

        return self.first.value

    def __len__(self):
        return self.size

    def __bool__(self):
        return bool(self.size)
