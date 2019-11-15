#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val < l2.val:
        node = l1
        node.next = mergeTwoLists(l1.next, l2)
        return node
    else:
        node = l2
        node.next = mergeTwoLists(l1, l2.next)
        return node


if __name__ == "__main__":
    import doctest
    doctest.testmod()
