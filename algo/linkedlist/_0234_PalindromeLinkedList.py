# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    #Time: O(N), Space: O(1)
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        count = 0
        cur = head
        # count the number of nodes
        while cur is not None:
            cur = cur.next 
            count += 1
        
        # special cases
        cur = head
        if count == 1:
            return True
        if count == 2:
            if cur.val == cur.next.val:
                return True
            else:
                return False
            
        # calculate the time we need to reverse (to the center)
        reverseCount = (count + 1 ) // 2 - 1 
        print("count:", count, "reverseCount:", reverseCount)
        
        # reverse the nodes until the center 
        p1, p2, p3 = head, head.next, head.next.next
        head.next = None 
        for i in range(reverseCount):
            p2.next = p1 
            p1 = p2 
            p2 = p3 
            p3 = p3.next 
        
        # decide the left and right to traverse out based on whether number of nodes is odd or even
        if count % 2 == 0: 
            pLeft = p1 
            pRight= p2
        else:
            pLeft = p1.next  #skip p1 which is the center
            pRight= p2
        
        # traverse out and compare 
        while pLeft is not None and pRight is not None:
            #print("pLeft:", pLeft.val, "pRight:", pRight.val)
            if pLeft.val != pRight.val:
                return False
            pLeft = pLeft.next
            pRight = pRight.next
        return True
            