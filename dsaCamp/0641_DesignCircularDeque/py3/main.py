#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None
        self.prev = None


class MyCircularDeque:
    """
    Official test case
    >>> cd = MyCircularDeque(3)
    >>> cd.insertLast(1)
    True
    >>> cd.insertLast(2)
    True
    >>> cd.insertFront(3)
    True
    >>> cd.insertFront(4)
    False
    >>> cd.getRear()
    2
    >>> cd.isFull()
    True
    >>> cd.deleteLast()
    True
    >>> cd.insertFront(4)
    True
    >>> cd.getFront()
    4

    >>> cd = MyCircularDeque(2)
    >>> cd.deleteFront()
    False
    >>> cd.deleteLast()
    False
    >>> cd.insertLast(1)
    True
    >>> cd.getFront()
    1
    >>> cd.getRear()
    1
    >>> cd.insertFront(2)
    True
    >>> cd.insertLast(3)
    False
    >>> cd.getFront()
    2
    >>> cd.getRear()
    1
    >>> cd.deleteFront()
    True
    >>> cd.deleteLast()
    True
    >>> cd.getFront()
    -1
    >>> cd.getRear()
    -1
    """

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """

        self.head, self.tail = ListNode(-1), ListNode(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.length = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """

        if self.isFull():
            return False
        new = ListNode(value)
        old = self.head.next
        self.head.next, new.prev = new, self.head
        new.next, old.prev = old, new
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """

        if self.isFull():
            return False
        new = ListNode(value)
        old = self.tail.prev
        self.tail.prev, new.next = new, self.tail
        old.next, new.prev = new, old
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """

        if self.isEmpty():
            return False
        old, new = self.head.next, self.head.next.next
        self.head.next, new.prev = new, self.head
        del old
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """

        if self.isEmpty():
            return False
        old, new = self.tail.prev, self.tail.prev.prev
        self.tail.prev, new.next = new, self.tail
        del old
        self.length -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """

        return self.head.next.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """

        return self.tail.prev.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """

        return self.length == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """

        return self.length == self.capacity


if __name__ == "__main__":
    import doctest
    doctest.testmod()
