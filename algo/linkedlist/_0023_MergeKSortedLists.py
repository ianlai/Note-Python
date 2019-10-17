# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    isDebug = False
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        heap = []
        valToHeadArr = {}
        valToIdxArr  = {}
        dummy = ListNode(-1)
        cur = dummy 
        remainingCounter = len(lists)
        
        while True:
            #heap push
            for i in range(len(lists)):
                head = lists[i]
                if head is None:
                    remainingCounter -= 1 
                    if remainingCounter == 0: 
                        return dummy.next 
                    continue
                
                self.debug("head: " + str(head.val))
                self.debug("remain:" + str(remainingCounter))
                value = head.val 
                self.debug()
                if value in valToHeadArr:
                    self.debug(str(value) + " in heap")
                    valToHeadArr[value].append(head)
                    valToIdxArr[value].append(i)
                else:
                    heapq.heappush(heap, value) #add to heap 
                    self.debug(str(value) + " is added to heap")
                    valToHeadArr[value] = [head] 
                    valToIdxArr[value] = [i]
                remainingCounter = len(lists)   #reset the remainingCounter 
                
            #find min 
            minHeadValue = heapq.heappop(heap)
            self.debug()
            self.debug("minHeadValue:" + str(minHeadValue))
            minHeadArr = valToHeadArr[minHeadValue]
            ###self.debug("minHeadArr:", minHeadArr)
            minIdxArr = valToIdxArr[minHeadValue]
            ###self.debug("minIdxArr:", minIdxArr)
            
            #attach to the result list 
            for minHead in minHeadArr:
                cur.next = ListNode(minHead.val) #new node
                cur = cur.next
            del valToHeadArr[minHeadValue]
            
            #remove the one which is attached to the result list 
            for minIdx in minIdxArr:
                self.debug("> minIdx:" + str(minIdx))
                lists[minIdx] = lists[minIdx].next
            del valToIdxArr[minHeadValue]
            
            #reset
            heap = []
            valToHeadArr = {}
            valToIdxArr  = {}
        
            #debug 
            d = dummy
            self.debug("result: ")
            while d:
                self.debug(str(d.val) + "-->")
                d = d.next
            self.debug()
            self.debug("=============")
    def debug(self, msg=""):
        if Solution.debug == True:
            print(msg)