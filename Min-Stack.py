1class MinStack:
2
3    def __init__(self):
4        self.stack = list()
5        self.min_vals = list()
6
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9        if not self.min_vals or self.min_vals[-1]>=val:
10            self.min_vals.append(val)
11
12    def pop(self) -> None:
13        val = self.stack.pop()
14        if val == self.min_vals[-1]:
15            self.min_vals.pop()
16        
17
18    def top(self) -> int:
19        return self.stack[-1]
20
21    def getMin(self) -> int:
22        return self.min_vals[-1]
23        
24
25
26# Your MinStack object will be instantiated and called as such:
27# obj = MinStack()
28# obj.push(val)
29# obj.pop()
30# param_3 = obj.top()
31# param_4 = obj.getMin()