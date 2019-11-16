#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def approach01MergeThenSort(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i, v in enumerate(nums2):
        nums1[m+i] = v
    nums1.sort()
    return


def approach03BackwardTwoPointer(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    idx, i1, i2 = (m+n-1), m-1, n-1
    while i1 >= 0 and i2 >= 0:
        if nums1[i1] > nums2[i2]:
            nums1[idx] = nums1[i1]
            idx, i1 = idx-1, i1-1
        else:
            nums1[idx] = nums2[i2]
            idx, i2 = idx-1, i2-1

    for i in range(i2+1):
        nums1[i] = nums2[i]

    return


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    # Official case
    >>> nums1 = [1,2,3,0,0,0]
    >>> merge(nums1, 3, [2,5,6], 3)
    >>> nums1 == [1,2,2,3,5,6]
    True

    # One array is empty.
    >>> nums1 = [1,2]
    >>> merge(nums1, 2, [], 0)
    >>> nums1 == [1,2]
    True

    >>> nums1 = [0,0,0]
    >>> merge(nums1, 0, [1,2,3], 3)
    >>> nums1 == [1,2,3]
    True
    """

    if n == 0:
        return

    approach03BackwardTwoPointer(nums1, m, nums2, n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
