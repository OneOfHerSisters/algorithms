1from collections import deque
2
3class Solution:
4    def predictPartyVictory(self, senate: str) -> str:
5        radiant = deque()
6        dire = deque()
7        n = len(senate)
8
9        for i, s in enumerate(senate):
10            if s == 'R':
11                radiant.append(i) 
12            else:
13                dire.append(i)  
14
15        while radiant and dire: 
16            r = radiant.popleft()
17            d = dire.popleft()
18
19            if r < d:
20                radiant.append(r + n)
21            else:
22                dire.append(d + n)
23
24        return "Radiant" if radiant else "Dire"
25
26        
27
28        