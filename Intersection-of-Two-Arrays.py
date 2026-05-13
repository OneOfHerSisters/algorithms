1from collections import Counter
2
3class Solution:
4    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
5        d1 = Counter(nums1)
6        d2 = Counter(nums2)
7        res = []
8        for key in d1:
9            if key in d2:
10                res.append(key)
11        return res
12
13
14        