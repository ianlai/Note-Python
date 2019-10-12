class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return []
        
        map = {}
        res = []
        
        for s in strs:
            key_str = ''.join(sorted(s))
            if key_str in map:
                map[key_str].append(s)
            else:
                map[key_str] = [s]
        
        for key in map:
            res.append(map[key])
            
        return res
            