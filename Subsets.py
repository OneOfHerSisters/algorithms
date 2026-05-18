1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        res = []
4
5        def backtrack(start, comb):
6            res.append(comb.copy())
7
8            for i in range(start, len(nums)):
9                comb.append(nums[i])
10                backtrack(i+1, comb)
11                comb.pop()
12        
13        backtrack(0, [])
14        return res
15
16
17
18
19        