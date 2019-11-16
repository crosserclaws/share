# 88. Merge Sorted Array

## Clarification

- 2 sorted arrays
  - Array1 has m elements.
  - Array2 has n elements.
- Modify and return Array1 as the result.

## Possible solutions

- Merge then sort.
  - Time: O((N+M)log(N+M)).
  - Space: O(1).
- Forward two pointer
  - Time: O(N+M)
  - Space: O(M).
- Backward two pointer
  - Time: O(N+M)
  - Space: O(1).
