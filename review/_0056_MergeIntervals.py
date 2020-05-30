class Solution:
    
    # Sort then 1-layer loop to merge [14%]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for interval in intervals:
            #Merged is not empty and current start is smaller than the end of last merged 
            if merged and interval[0] <= merged[-1][1]: 
                merged[-1][1] = max(interval[1], merged[-1][1]) 
            else:
                merged.append(interval)
        return merged
    
    #===================================================================
    
    # Sort then 2-layer loops to merge [14%]
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        
        intervals.sort(key=lambda x: x[0])  #in-place; it's also fine without the key
        print(intervals)
        ans = []
        
        #This number is to skip the merged intervals (skip how many times we can arrive the target)
        #e.g. 1st round -> [1,3] ; it merged [2,6]
        #     2nd round -> we should skip [2,6] and start from [8,10]
        skipNumber = 0
        for i in range(len(intervals)):
            if skipNumber > 0:
                skipNumber -= 1
                continue
            start, end = intervals[i][0], intervals[i][1] #target
            newEnd = end 
            #print("s, new e = ", start, newEnd)
            for j in range(i+1, len(intervals)):
                innerStart, innerEnd = intervals[j][0], intervals[j][1]
                #print(" >> inner s, e = ", innerStart, innerEnd)
                if innerStart <= newEnd: #merge, remove j interval 
                    #print(" >> merge")
                    newEnd = max(newEnd, innerEnd)
                    skipNumber += 1
                else:
                    #print(" >> not merge")
                    break
            ans.append([start, newEnd])
        return ans