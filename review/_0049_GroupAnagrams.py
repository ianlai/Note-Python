class Solution:
    
    # Use bit map of string as the key [O(N*L), 48%-57%]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print("bit map")
        if not strs:
            return []
        
        keyToStrList = collections.defaultdict(list)
        ans = []
        
        for s in strs:
            bitMap = self.getBitMap(s)
            keyToStrList[bitMap].append(s)
        
        for key in keyToStrList:
            ans.append(keyToStrList[key])
        
        return ans
            
    def getBitMap(self, s):
        bitMap = [0] * 26
        ordA = 97
        for char in s:
            idx = ord(char) - ordA 
            bitMap[idx] += 1
        return tuple(bitMap)
        
    # ===========================================================
    
    # Use sorted string as the key [O(N*LlogL), 18%-24%]
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        print("sort")
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
            