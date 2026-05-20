1class Solution:
2    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
3        res = []
4        comb = []
5
6        def backtracking(start, n):
7            if len(comb) == k:
8                if n == 0:
9                    res.append(comb.copy())
10                return
11
12            for i in range(start, 10):
13                if i > n:
14                    break
15
16                comb.append(i)
17                backtracking(i + 1, n - i)
18                comb.pop()
19
20        backtracking(1, n)
21        return res