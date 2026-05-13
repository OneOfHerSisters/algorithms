1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l = 0
4        r = len(height) - 1
5        max_res = 0
6        while l < r:
7            s = (r - l) * min(height[l], height[r])
8            max_res = max(max_res, s)
9            if height[l] <= height[r]:
10                l += 1
11            else:
12                r -= 1
13        return max_res
14            
15        