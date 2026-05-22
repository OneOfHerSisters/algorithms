1class Solution:
2    def fib(self, n: int) -> int:
3        if n < 2:
4            return n
5
6        res = 1
7        a = 0
8        b = 1
9        
10        for i in range(2, n+1):
11            res = a + b
12            a = b
13            b = res
14            
15        return res
16        