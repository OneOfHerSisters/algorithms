1class Solution:
2    def summaryRanges(self, nums: List[int]) -> List[str]:
3        left = 0
4        right = 0
5        res = []
6        while right < len(nums):
7            if right != (len(nums) - 1) and nums[right+1]-nums[right] == 1:
8                right += 1
9            else:
10                res.append(f"{nums[left]}" if right-left == 0 else f"{nums[left]}->{nums[right]}")
11                right += 1
12                left = right
13                
14        return res
15
16
17        