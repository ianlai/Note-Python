# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = []
        while head != None:
            arr.append(head)
            head = head.next
        return arr[len(arr)//2]