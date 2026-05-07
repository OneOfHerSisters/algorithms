1class Solution:
2    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        d1 = {}
4        d2 = {}
5        res = []
6        for elem in nums1:
7            d1[elem] = d1.get(elem, 0) + 1
8        for elem in nums2:
9            d2[elem] = d2.get(elem, 0) + 1
10        for key, value in d1.items():
11            if key in d2:
12                for _ in range(min(d1[key], d2[key])):
13                    res.append(key)
14        return res
15
16        