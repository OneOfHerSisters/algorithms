1import time
2from collections import deque
3
4class RecentCounter:
5
6    def __init__(self):
7        self.queue = deque()
8        
9    def ping(self, t: int) -> int:
10        self.queue.append(t)
11
12        while self.queue[0] < t - 3000:
13            self.queue.popleft()
14
15        return len(self.queue)
16
17# Your RecentCounter object will be instantiated and called as such:
18# obj = RecentCounter()
19# param_1 = obj.ping(t)