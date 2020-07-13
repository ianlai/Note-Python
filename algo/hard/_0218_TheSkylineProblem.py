import functools 
class Solution:
        
    # Reference:    
    # https://www.youtube.com/watch?v=GSBLe8cKu0s

    # Cases: 
    # [[1,3,3],[2,4,4],[5,8,2],[6,7,4],[8,9,4]]  
    # [[6,7,2],[7,8,3]]
    # [[0,2,3],[2,5,3]]  //failed

    # Define comparator, calculate the max and pre-max [10%]
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        print("Mine")
        
        if not buildings:
            return []
        
        points = []
        ans = []
        
        # Loop the buildings and create the point list (double of buildings)
        for b in buildings:
            point = [b[0], b[2], 1] #start
            points.append(point)
            point = [b[1], b[2], 0] #end
            points.append(point)
        
        # Comparator-1 (ok) 
        def sortedBy1(a, b):                
            if a[0] != b[0]:          #different x
                return a[0] - b[0]    #asc 
            if a[2] == 1 and b[2] == 1:   #both start
                return b[1] - a[1]        #dsc
            if a[2] == 0 and b[2] == 0:       #both end
                return a[1] - b[1]            #asc
            if b[2] == 1:                         #start and end
                return 1                          #"end" goes first
            else:
                return -1
        
        # Comparator-2 (ok) 
        def sortedBy2(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                p, q = 0, 0
                if a[2] == 1:
                    p = -a[1] 
                else:
                    p = a[1]
        
                if b[2] == 1:
                    q = -b[1]
                else:
                    q = b[1]
                return p - q
        
        # We need to use the functools (in Python3) to define a full comparator (not just lambda)
        cmp = functools.cmp_to_key(sortedBy1)
        points.sort(key = cmp)
        print("Points:", points)
        print()
        
        # Method-1: Use an queue to store the count of max (ok)
        # Queue stores the mapping between 
        queue = {}
        queue[0] = 1 #put a dummy node [0, 1] meaning 1 height=0 inside
        prevMax = 0 
        
        # Loop the points 
        # If it is start point, if y is in queue, add by 1, 
        #                       if y is not in queue, set it to 1
        # If it is end point, if there is more than 1 y, deduct by 1
        #                     if only 1 y, remove it (impossible to have no y since it's an end point)
        
        for p in points:
            x, y = p[0], p[1]
            
            if p[2] == 1: #start
                if y in queue:
                    queue[y] += 1
                else:
                    queue[y] = 1
                    
            else:         #end 
                if queue[y] > 1:
                    queue[y] -= 1
                else:
                    del queue[y]
 
            #If the current max differs from the prev max, then add the point into ans
            currMax = max(queue.keys())  # O(n)
            if prevMax != currMax:
                ans.append([x, currMax])
                prevMax = currMax
            
        # Method-2: Use an array to store the max (wrong)
#         for p in points:
#             print(p, maxHeights)
#             if p[2] == 1:  #start
                
#                 location = len(maxHeights)
#                 for i in range(len(maxHeights)):
#                     if p[1] < maxHeights[i]:
#                         location = i
#                         break
#                 if p[1] not in maxHeights:
#                     maxHeights.insert(location, p[1])
                    
#                 maxHeight = maxHeights[-1]
#                 if p[1] == maxHeight:
#                     ans.append([p[0], p[1]])
#             else:
#                 if p[1] in maxHeights:
#                     maxHeights.remove(p[1])
                    
#                 maxHeight = maxHeights[-1] 
#                 if p[1] >= maxHeight:
#                     ans.append([p[0], maxHeight])        
#             print("Ans:", ans)
#             print()

        return ans
            
            