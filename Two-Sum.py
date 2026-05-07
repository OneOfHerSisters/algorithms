1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        d = {}
4        for i in range(len(nums)):
5            if (target - nums[i]) in d:
6                return (d[target - nums[i]], i)
7            else:
8                d[nums[i]] = i
9
10            
11
12
13
14        