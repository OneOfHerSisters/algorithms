1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5        
6        while left <= right:
7            middle = left + (right-left)//2
8
9            if nums[middle] == target:
10                return middle
11            if nums[middle] < target:
12                left = middle + 1
13            elif nums[middle] > target:
14                right = middle - 1
15        return left
16        
17        