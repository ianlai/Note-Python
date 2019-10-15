class Solution:
    
    # Use min heap to solve (direct way) 
    # The reason to use min heap is (1) algorithm simple, (2) python's heapq only supports min heap
    # Note: since we don't only return the top Kth values, but only the top Kth points, 
    # we need a structure to record the points (hashmap)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if points == None: 
            return []
        
        distances = []
        d2ps = {}          #distance to point
        ans = []
        
        
        for p in points:
            d = p[0] ** 2 + p[1] ** 2  #without sqrt 
            #distances.append(d)     
            if d in d2ps:            
                d2ps[d].append(p)      #add a new point to an existing array
            else: 
                distances.append(d)    #if this distance is not in array yet, add a distance 
                d2ps[d] = [p]          #add a new point to new array into the value of that distance
        
        heapq.heapify(distances)
        while len(ans) < K:  
            min_distance = heapq.heappop(distances)
            min_points = d2ps[min_distance]
            ans.extend(min_points)     #add as a group
            print(min_distance, ":", min_points)
        
        while len(ans) > K:            #because it's added as a group, it might more than the requirement
            ans.pop()

        return ans
            