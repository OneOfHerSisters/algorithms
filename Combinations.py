1class Solution:
2    def combine(self, n: int, k: int) -> List[List[int]]:
3        res = []
4
5        def backtrack(start, comb):
6            if len(comb) == k:
7                res.append(comb.copy())
8                return
9            for i in range(start, n+1):
10                comb.append(i)
11                backtrack(i+1, comb)
12                comb.pop()
13            
14        backtrack(1, [])
15        return res