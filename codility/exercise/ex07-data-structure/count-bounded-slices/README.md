# CountBoundedSlices <!-- omit in toc -->

## Table of content <!-- omit in toc -->
- [Basic solution](#basic-solution)
- [Enhanced solution](#enhanced-solution)
- [Optimal solution](#optimal-solution)
- [Resources](#resources)


## Basic solution

## Enhanced solution

## Optimal solution

Idea
- If a slice [i, j] is bounded, then every slice [i+1, j], [i+2, j], ..., [j, j] is bounded too.
- Sliding window like approach to calculate the number.
- Maintain min/max monotonic double-ended queue to get min/max instantly.

Complexity
- Time: O(N)
- Space: O(N)

## Resources

- [Official solution](./resources/solution-count-bounded-slices.pdf)
- Great [explanation](https://www.careercup.com/question?id=5090693043191808) at CareerCup
