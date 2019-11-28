class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if A is None or len(A) == 0:
            return []
        
        statistics = []
        ans = []
        for string in A:
            map = {}
            for c in string:
                if c in map:
                    map[c] += 1
                else:
                    map[c] = 1 
            statistics.append(map)
        
        
        for c in "abcdefghijklmnopqrstuvwxyz":
            minValue = 99999
            for map in statistics:
                if c in map:
                    minValue = min(map[c], minValue)
                else:
                    minValue = 0
            for i in range(minValue):
                ans.append(c)
            
        return ans