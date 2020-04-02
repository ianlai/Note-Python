import heapq
class Solution:

    # Heap approach: O(nlogn) -> 30%
    # >> Sorting: O(nlogn)
    # >> N time of min of end time: O(nlogn)
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key= lambda x: x[0]) #sort by start time
        heap = [intervals[0][1]]            #min-heap of end time 
        #print("intervals:", intervals)
        
        for interval in intervals[1:]: #start from 1, not 0
            earliestEnd = heap[0]  #earlist end time 
            if earliestEnd <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        #print("endTimes:", heap)
        return len(heap)
    
    # =========================================================
    
    # Basic approach: O(n2) -> 30% 
    # >> Sorting: O(nlogn)
    # >> N time of finding smaller meeting room: O(n2)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort()
        #print(intervals)
        meetingRooms = []
        for interval in intervals:
            inserted = False
            for room in meetingRooms: 
                if room[-1][1] <= interval[0]:
                    room.append(interval)
                    inserted = True
                    break    #only insert into one room
            if not inserted:
                meetingRooms.append([]) #new room
                meetingRooms[-1].append(interval)
        #print(meetingRooms)
        return len(meetingRooms)
                
            
        