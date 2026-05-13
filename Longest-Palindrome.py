1class Solution:
2    def longestPalindrome(self, s: str) -> int:
3        letters_count = {}
4        res = 0
5        has_odd = False
6        for letter in s:
7            letters_count[letter] = letters_count.get(letter, 0) + 1
8        for count in letters_count.values():
9            res += count - (count % 2)
10            if count % 2:
11                has_odd = True
12        return res + (1 if has_odd else 0)
13