class Solution:
    
    # Sliding window with a set  [O(n), 45%]
    def lengthOfLongestSubstring(self, s: str) -> int:
        print("sliding window")
        if not s or len(s) == 0:
            return 0
        
        charSet = set()
        maxCount = 0 
        start, end = 0, 0 
        while end != len(s):
        
            if s[end] in charSet:
                # while s[start] != s[end]:
                #     start += 1
                # start += 1
                # end += 1
                charSet.remove(s[start])
                start += 1
                
            else:
                charSet.add(s[end])
                end += 1
                
            # if end == len(s):
            #     break
                
            maxCount = max(maxCount, end - start)
                
            # print(start, end, charSet)
            # print(maxCount)
            # print()
        return maxCount
    
    #===============================================
    
    # Use a set  [O(n2), 7%]
    def lengthOfLongestSubstring2(self, s: str) -> int:
        print("set")
        if s is None or len(s) == 0 :
            return 0
        
        maxCount = 0 
        for i in range(len(s)):
            chatSet = set()
            
            for j in range(i, len(s)):
                cur = s[j]
                if cur not in chatSet:
                    chatSet.add(cur)
                    maxCount = max(maxCount, len(chatSet))
                else:
                    maxCount = max(maxCount, len(chatSet))
                    break
                    
        return maxCount
    
    #===============================================
    
    # Use a map  [O(n2), 7%]
    def lengthOfLongestSubstring1(self, s: str) -> int:
        print("map")
        if s is None or len(s) == 0 :
            return 0
        
        maxCount = 0 
        for i in range(len(s)):
            charMap = {}
            
            for j in range(i, len(s)):
                cur = s[j]
                if cur not in charMap:
                    charMap[cur] = 1
                    maxCount = max(maxCount, len(charMap))
                else:
                    maxCount = max(maxCount, len(charMap))
                    break
                    
        return maxCount