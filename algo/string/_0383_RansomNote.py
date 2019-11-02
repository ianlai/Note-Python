class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0:
            return True
        if len(magazine) < 0:
            return False
        
        map = {}
        for e in magazine:
            if e in map:
                map[e] += 1
            else:
                map[e] = 1
        
        
        for e in ransomNote:
            #print(map)
            if e not in map:
                return False
            else:
                map[e] -= 1
                if map[e] < 0:
                    return False
        return True