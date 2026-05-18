1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res = []
4        curr = []
5        candidates.sort() 
6        
7        def backtrack(start, remaining):
8            if remaining == 0:
9                res.append(curr.copy())
10                return
11            for i in range(start, len(candidates)):
12                if candidates[i] > remaining:
13                    break 
14                curr.append(candidates[i])
15                backtrack(i, remaining - candidates[i])
16                curr.pop()
17        
18        backtrack(0, target)
19        return res