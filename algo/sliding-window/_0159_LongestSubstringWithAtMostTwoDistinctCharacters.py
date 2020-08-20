class Solution:
    
    # Sliding window [9%]
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        if len(s) < 3:
            return len(s)
        #charToCount = collections.defaultdict(int)
        charToCount = {}
        start, end = 0, 0
        maxLength = 2
        duplicateCount = 0
        
        while end < len(s):
            print(start, end, charToCount)
            #if duplicateCount > 2:
            if len(charToCount) < 3: 
                charToCount[s[end]] = end
                end += 1
            
            if len(charToCount) == 3: 
                # if charToCount[s[start]] == 2:
                #     duplicateCount -= 1   
                # if charToCount[s[start]] == 1:
                #     del charToCount[s[start]]
                # else:    
                #     charToCount[s[start]] -= 1
                delIdx = min(charToCount.values())
                del charToCount[s[delIdx]]
                start = delIdx + 1
                # start += 1 
#             else:
#                 # if charToCount[s[end]] == 1:
#                 #     duplicateCount += 1
                
#                 # if s[end] in charToCount:
#                 #     charToCount[s[end]] += 1
#                 # else:
#                 #     charToCount[s[end]] = 1
#                 charToCount[s[end]] = end
#                 end += 1
            
            maxLength = max(maxLength, end - start)
        
        return maxLength
                
                