1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8        maxSum = float('-inf')
9        fast = head
10        slow = head
11        
12        while fast and fast.next is not None:
13            slow = slow.next
14            fast = fast.next.next
15
16        curr = slow
17        prev = None
18
19        while curr:
20            temp = curr.next
21            curr.next = prev
22            prev = curr
23            curr = temp
24
25        right = prev
26        left = head
27
28        while right:
29            if right.val + left.val > maxSum:
30                maxSum = right.val + left.val
31            right = right.next
32            left = left.next 
33
34        return maxSum
35
36        
37
38        
39
40        
41
42        
43
44        
45        