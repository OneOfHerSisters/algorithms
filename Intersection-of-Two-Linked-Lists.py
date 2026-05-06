1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
9        a = headA
10        b = headB
11        
12        while a is not b:
13            a = a.next if a else headB
14            b = b.next if b else headA
15        
16        return a
17        
18
19
20
21        
22
23
24        