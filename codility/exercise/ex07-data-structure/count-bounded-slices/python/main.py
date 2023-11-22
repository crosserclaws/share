from collections import deque
from dataclasses import dataclass


def solution(K: int, A: list[int]):
    n = len(A)
    MAX_NUM = 1_000_000_000
    minQ, maxQ = deque(), deque()
    count = j = 0
    for i in range(n):
        while j < n:
            # Descending order
            while maxQ and maxQ[-1].val <= A[j]:
                maxQ.pop()
            maxQ.append(QueueItem(j, A[j]))
            # Ascending order
            while minQ and minQ[-1].val >= A[j]:
                minQ.pop()
            minQ.append(QueueItem(j, A[j]))

            if maxQ[0].val - minQ[0].val > K:
                break
            j += 1
        count += j - i
        if count >= MAX_NUM:
            return MAX_NUM
        if maxQ[0].idx == i:
            maxQ.popleft()
        if minQ[0].idx == i:
            minQ.popleft()
    return count


@dataclass
class QueueItem:
    idx: int
    val: int
