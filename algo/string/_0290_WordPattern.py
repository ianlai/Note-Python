class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pToS = {}
        sToP = {}
        strList = str.split()
        
        #lengths are different 
        if len(strList) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            p = pattern[i]
            s = strList[i]
            
            # new pattern and new string -> add new pair
            if p not in pToS and s not in sToP:
                pToS[p] = s
                sToP[s] = p
            # old pattern -> check this pattern fits the string
            elif p in pToS: 
                if s != pToS[p]:
                    return False
            # new pattern and old string -> invalid 
            else:
                return False
            
        return True
            