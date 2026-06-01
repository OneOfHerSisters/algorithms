1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        now = head
9        prev = None 
10
11        while now:
12            tmp = now.next
13            now.next = prev
14            prev = now
15            now = tmp
16
17        return prev
18            
19
20
21        