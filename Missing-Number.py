1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        s = 0
4        for i in range(len(nums)):
5            s += nums[i]
6        return sum(range(len(nums) + 1)) - s
7
8        