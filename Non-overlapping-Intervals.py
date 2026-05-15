1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x: x[1])
4        removed = 0
5        last_end=float('-inf')
6
7        for start, end in intervals:
8            if start >= last_end:
9                last_end = end
10            else:
11                removed += 1
12
13        return removed
14
15
16        