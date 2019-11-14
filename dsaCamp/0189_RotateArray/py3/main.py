#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def approach01Move(nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    if n < 2 or k == 0:
        return True

    for _ in range(k):
        prev = nums[-1]
        for i, v in enumerate(nums):
            prev, nums[i] = v, prev
    return


def approach02Copy(nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    if n < 2 or k == 0:
        return True

    nums[:k], nums[k:] = nums[-k:], nums[:-k]
    return


def approach03CyclicReplacements(nums: List[int], k: int) -> None:
    pass


def approach04Reverse(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    if n < 2 or k == 0:
        return True

    def reverse(nums: List[int], start: int, end: int) -> None:
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1

    nums.reverse()
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    return


def rotate(nums: List[int], k: int) -> None:
    approach04Reverse(nums, k)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
