class Solution:
    
    # Backtracking: Slice approach (51%)
    def wordPatternMatch(self, pattern: str, string: str) -> bool:
        def helper(pattern, string, mapping, used):
            if not pattern:
                return not string

            p = pattern[0]
            if p in mapping:
                word = mapping[p]
                if not string.startswith(word):
                    return False
                return helper(pattern[1:], string[len(word):], mapping, used)

            for i in range(len(string)):
                word = string[:i+1]
                if word in used:
                    continue

                used.add(word)
                mapping[p] = word

                if helper(pattern[1:], string[i+1:], mapping, used):
                    return True

                del mapping[p]
                used.remove(word)
            return False
    
        return helper(pattern, string, {}, set())

    # Backtracking: Index approach (22%)
    def wordPatternMatch1(self, pattern: str, string: str) -> bool:
        def helper(patterns, string, pi, si, pToS, sToP):
            #print(pi,", ", si)
            
            if len(patterns) == 0 and len(string) == 0: 
                return True
            if len(patterns) == 0 and len(string) != 0: 
                return False
            if len(patterns) != 0 and len(string) == 0: 
                return False
            if len(patterns) == 1: 
                return True
            
            if pi == len(patterns) and si == len(string):
                return True
            if pi == len(patterns) or si == len(string):
                return False

            p = patterns[pi]
            if p in pToS:
                word = pToS[p]
                newString = string[si:si+len(word)]
                if newString != word: 
                    return False
                return helper(patterns, string, pi+1, si+len(word), pToS, sToP)
            else:
                for i in range(si, len(string)): #remove -1
                    word = string[si:i+1]
                    if word in sToP:
                        continue

                    sToP[word] = p
                    pToS[p] = word

                    if helper(patterns, string, pi+1, si+len(word), pToS, sToP):
                        return True

                    del pToS[p]
                    del sToP[word]
                return False

        return helper(pattern, string, 0, 0, {}, {})

            
    #Backtracking (Index approach) 
    def wordPatternMatch2(self, pattern: str, str: str) -> bool:
        return self.helper(pattern, str, 0, 0, {}, {})
    
    def helper(self, patterns, string, pi, si, pToS, sToP):
        print(pi,",", si, end="    ")
        if pi == len(patterns) and si == len(patterns):
            return True
        if pi == len(patterns) or si == len(patterns):
            return False
        
        p = patterns[pi]
       
        if p in pToS: #existing pattern
            print("existing pattern: ", p, " | ", end = "")
            storedStr = pToS[p]
            print("storedStr:", storedStr, " pStr:", string[si:si+len(storedStr)], end ="  ")
            if string[si:si+len(storedStr)] != storedStr: 
                print("mismatch")
                return False
            else:
                print("match, keep searching")
                return self.helper(patterns, string, pi+1, si+len(storedStr), pToS, sToP)  
        else:         #new pattern
            for j in range(si+1, len(string)):
                print("new pattern: ", p, " | ", end = "")
                newStr = string[si:j]
                print("newStr:   ", newStr)
                if newStr in sToP:
                    return False
                pToS[p] = newStr
                sToP[newStr] = p
                if self.helper(patterns, string, pi+1, si+len(newStr), pToS, sToP):
                    return True
                del pToS[p]
                del sToP[newStr]
            return False
            
            

# class Solution:
#     def wordPatternMatch(self, pattern: str, str: str) -> bool:
#         return self.helper(pattern, str, 0, 0, {}, {})
    
#     def helper(self, patterns, string, pi, si, pToS, sToP):
#         print(pi, si)
#         if pi == len(patterns) and si == len(patterns):
#             return True
#         if pi == len(patterns) or si == len(patterns):
#             return False
        
#         for i in range(pi, len(patterns)):
#             p = patterns[i]
#             print("pattern: ", p, " | ", end = "")
#             if p in pToS: #existing pattern
#                 storedStr = pToS[p]
#                 print("storedStr:", storedStr, " pStr:", string[si:si+len(storedStr)])
#                 if string[si:si+len(storedStr)] != storedStr: 
#                     return False
#                 else:
#                     return self.helper(patterns, string, pi+1, si+len(storedStr), pToS, sToP)  
#             else:         #new pattern
#                 for j in range(si+1, len(string)):
#                     newStr = string[si:j]
#                     print("newStr:   ", newStr)
#                     if newStr in sToP:
#                         return False
#                     pToS[p] = newStr
#                     sToP[newStr] = p
#                     if self.helper(patterns, string, pi+1, si+len(newStr), pToS, sToP):
#                         return True
#                     del pToS[p]
#                     del sToP[newStr]
            
        