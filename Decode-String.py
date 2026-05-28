1class Solution:
2    def decodeString(self, s: str) -> str:
3        stringStack = []
4        digitStack = []
5        cur = ""
6        k = 0
7
8        for c in s:
9            if c.isdigit():
10                k = k*10 + int(c)
11            elif c == "[":
12                digitStack.append(k)
13                stringStack.append(cur)
14                cur = ""
15                k = 0
16            elif c == "]":
17                prev = stringStack.pop()
18                times = digitStack.pop()
19                cur = prev + cur*times
20            else:
21                cur += c
22        
23        return cur
24                
25                
26            
27
28
29
30        