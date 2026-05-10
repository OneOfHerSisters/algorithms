1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        for i in range(len(matrix)):
4            for j in range(i+1, len(matrix)):
5                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
6            
7        for row in matrix:
8            row.reverse()
9
10        return matrix
11
12                
13        