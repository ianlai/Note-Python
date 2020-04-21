class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        mset = set([])
        for e in arr:
            count[e] = count.get(e, 0) + 1 
        for k in count:
            val = count[k]
            if val in mset:
                return False
            mset.add(val)
        return True