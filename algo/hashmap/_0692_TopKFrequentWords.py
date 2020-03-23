import collections 

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or k == 0:
            return []
        
        cnt = collections.Counter(words)
        sortedCntKV = sorted(cnt.items(), key = lambda f: (-f[1], f[0])) #sort by count then alphabet 
        sortedCnt = [kv[0] for kv in sortedCntKV]
        ans = sortedCnt[:k]
        return ans