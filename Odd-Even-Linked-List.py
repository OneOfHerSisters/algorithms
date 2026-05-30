1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        odd = head
9
10        if head is None or head.next is None:
11            return head
12
13        even = head.next
14        evenHead = even
15
16        while even and even.next:
17            odd.next = even.next
18            odd = odd.next
19
20            even.next = odd.next
21            
22            even = even.next
23
24        odd.next = evenHead
25        
26        return head
27        