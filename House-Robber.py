1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        prev1 = 0
4        prev2 = 0
5        curr = 0
6
7        for i in range(len(nums)):
8            if nums[i]+prev2 > prev1:
9                curr = nums[i]+prev2
10            else:
11                curr = prev1
12            prev2 = prev1
13            prev1 = curr
14        
15        return curr
16        