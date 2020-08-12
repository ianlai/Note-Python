class Solution:
    
    # 3 layer loop [O(NNL), 48%-67%]
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if len(strings) == 0:
            return []
        
        def isShiftedStrings(s1, s2):
            if len(s1) != len(s2):
                return False
            diff = ord(s1[0]) - ord(s2[0]) 
            for i in range(len(s1)):
                if (ord(s1[i]) - ord(s2[i]) != diff and 
                ord(s1[i]) - ord(s2[i]) + 26 != diff and  
                ord(s1[i]) - ord(s2[i]) - 26 != diff):
                    return False
            return True
                
        resList = []
        isNewGroup = True
        
        for newStr in strings:
            for storedStrs in resList:
                storedStr = storedStrs[0]
                if isShiftedStrings(newStr, storedStr):
                    storedStrs.append(newStr)
                    isNewGroup = False
                    break
            if isNewGroup:
                resList.append([newStr])
            isNewGroup = True
                    
        return resList
    