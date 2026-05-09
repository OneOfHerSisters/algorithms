1class Solution:
2    count = 0
3
4    def visitSosed(self, g: List[List[str]], i :int, j : int):
5        if 0 <= i < len(g) and 0 <= j < len(g[i]) and g[i][j] == "1":
6            g[i][j] = "0"
7            self.visitSosed(g,i,j+1)
8            self.visitSosed(g,i+1,j)
9            self.visitSosed(g,i-1,j)
10            self.visitSosed(g,i,j-1)
11        else:
12            return
13
14    def numIslands(self, grid: List[List[str]]) -> int:
15        self.count = 0
16        for i in range(len(grid)):
17            for j in range(len(grid[i])):
18                if grid[i][j] == "1":
19                    self.count += 1
20                    self.visitSosed(grid, i, j)
21        return self.count
22         
23        