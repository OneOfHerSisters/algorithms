1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        stack = []
4
5        for asteroid in asteroids:
6            alive = True
7
8            while alive and asteroid < 0 and stack and stack[-1] > 0:
9                if stack[-1] < abs(asteroid):
10                    stack.pop()
11                else:
12                    if stack[-1] == abs(asteroid):
13                        stack.pop()
14                    alive = False
15
16            if alive:
17                stack.append(asteroid)
18
19        return stack