class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort()  #in-place
        ans = []
        skipNumber = 0
        for i in range(len(intervals)):
            if skipNumber > 0:
                skipNumber -= 1
                continue
            start, end = intervals[i][0], intervals[i][1]
            newEnd = end 
            #print("s, new e = ", start, newEnd)
            for j in range(i+1, len(intervals)):
                innerStart, innerEnd = intervals[j][0], intervals[j][1]
                #print(">> inner s, e = ", innerStart, innerEnd)
                if innerStart <= newEnd: #merge, remove j interval 
                    newEnd = max(newEnd, innerEnd)
                    skipNumber += 1
                else:
                    break
            ans.append([start, newEnd])
        return ans