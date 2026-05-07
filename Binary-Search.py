1class Solution:
2    def search(self, nums: list[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5
6        while left <= right:
7            middle = left + (right - left) // 2
8            if nums[middle] < target:
9                left = middle + 1
10            elif nums[middle] > target: 
11                right = middle - 1
12            else:
13                return middle
14                
15        return -1
16