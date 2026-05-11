1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int: 
3        curr_sum = max_sum = nums[0]
4
5        for i in range(1, len(nums)):
6            curr_sum = max(curr_sum + nums[i], nums[i])
7            max_sum = max(curr_sum, max_sum)
8        return max_sum
9        
10
11        