#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def isPalindrome(s: str) -> bool:
    """
    >>> isPalindrome("A man, a plan, a canal: Panama")
    True
    >>> isPalindrome("race a car")
    False
    >>> isPalindrome("")
    True
    """
    filtered = re.sub(r'\W+', '', s).lower()
    return filtered == filtered[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
