1class Solution:
2    def equalPairs(self, grid: List[List[int]]) -> int:
3        columns = [[] for _ in range(len(grid))]
4        res = 0
5
6        for i in range(len(grid)):
7            for j in range(len(grid[i])):
8                columns[j].append(grid[i][j])
9            
10        for row in grid:
11            for col in columns:
12                if row == col:
13                    res += 1
14        
15        return res
16
17        