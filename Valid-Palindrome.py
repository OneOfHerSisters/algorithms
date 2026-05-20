1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        new_s = [letter for letter in s.lower() if letter.isalnum()]
4        
5        left = 0
6        right = len(new_s) - 1
7        
8        while left <= right:
9            if new_s[left] != new_s[right]:
10                return False
11            left += 1
12            right -= 1
13        
14        return True
15        