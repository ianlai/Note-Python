class Solution:
    
    #Hashmap to count, sort by the occurrence [53%-81%]
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        sortedCounter = sorted(counter.items(), key = lambda x: -x[1])
        
        ans = []
        for char, cnt in sortedCounter:
            for j in range(cnt):
                ans.append(char)
        
        return ''.join(ans)