class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.isAnagram_map1(s, t)
    
    # Hashmap (if-else)
    def isAnagram_map1(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        
        for e in s:
            if e in map1: 
                map1[e] += 1
            else:
                map1[e] = 1
        
        for e in t:
            if e in map2: 
                map2[e] += 1
            else:
                map2[e] = 1
                
        return map1 == map2 
    
    # Hashmap (get function)
    def isAnagram_map2(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        
        for e in s: 
            map1[e] = map1.get(e,0) + 1
        
        for e in t:
            map2[e] = map2.get(e,0) + 1
                
        return map1 == map2 
            
    # Sort
    def isAnagram_sorted(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)