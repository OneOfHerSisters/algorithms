class Solution:
    def max_power(self, s: str) -> int:
        result = 1
        left = 0

        for right in range(1, len(s)):
            if s[left] != s[right]:
                left = right
            result = max(result, right - left + 1)

        return result
