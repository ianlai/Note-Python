class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if len(J) == 0 or len(S) == 0:
            return 0
        
        jewelToNum = {}
        for e in J:
            jewelToNum[e] = 0
        
        count = 0
        for e in S:
            if e in jewelToNum:
                count += 1
        
        return count 
        