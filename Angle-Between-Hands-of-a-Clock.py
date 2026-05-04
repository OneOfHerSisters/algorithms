1class Solution:
2    def angleClock(self, hour: int, minutes: int) -> float:
3        angle = abs(hour*30 - minutes*5.5)
4        return min(angle, 360-angle)
5
6        