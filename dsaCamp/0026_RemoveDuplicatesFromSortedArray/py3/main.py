#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    >>> removeDuplicates([])
    0
    >>> removeDuplicates([1])
    1
    >>> removeDuplicates([1,1,2])
    2
    >>> removeDuplicates([1, 2, 3])
    3
    >>> removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    5
    """

    last = 0
    for i, v in enumerate(nums):
        if v != nums[last]:
            last += 1
            nums[last] = v
    del nums[last+1:]
    return len(nums)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
