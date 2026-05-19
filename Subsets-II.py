1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        nums.sort()
5        
6
7        def backtracking(start, comb):
8            res.append(comb.copy())
9
10            for i in range(start, len(nums)):
11                if i > start and nums[i] == nums[i-1]:
12                    continue 
13                comb.append(nums[i])
14                backtracking(i+1, comb)
15                comb.pop()
16
17            return res
18
19        return backtracking(0, [])
20
21
22        
23                
24
25        