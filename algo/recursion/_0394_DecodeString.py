class Solution:
    
    # ================== Extract the parts with number ==================
    # Recursion separates in different functions 
    # Good practice
    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return s
        segment = self.separate(s) 
        
        if len(segment) > 0:
            return self.formString(s, segment)
        return s
   
    # Return an array of brackets (repeated number, left bracket, right bracket) in the current layer 
    # Use this function to handle multiple brackets 
    def separate(self, s):
        print("separate:", s)
        numBracketClosed = 0
        isDigitContinuous = False
        segments = [] #number, leftbracketidx, rightbrackidx
        j = 0
        for i in range(len(s)):
            if j > i:
                continue
            if s[i].isdigit() and numBracketClosed == 0:
                j = i + 1
                idxDigitStart = i
                curNumber = s[i]
                while s[j].isdigit(): 
                    curNumber += s[j]
                    j += 1 
                curNumber = int(curNumber)
            elif s[i] == '[':
                numBracketClosed += 1
                if numBracketClosed == 1:
                    idxLeftBracket = i
            elif s[i] == ']':
                numBracketClosed -= 1  
                if numBracketClosed == 0:
                    idxRightBracket = i
                    segments.append((curNumber, idxLeftBracket, idxRightBracket))              
        return segments
    
    # Based on the segments argument, formString handles the details of the string including 
    # (1) removing the number and brackets 
    # (2) call the decode function to start the recursion 
    # (3) concatenate each part of the strings 
    def formString(self, s, segments):
        print("formString:", s, segments)
        response = ""
        
        for i in range(len(segments)):
            num = segments[i][0]
            left = segments[i][1]
            right = segments[i][2]
            idxDigitStart = left - len(str(num))
            idxDigitEnd = left - 1
            if i == 0:
                response += s[:idxDigitStart]
                response += self.decode(s[left+1:right], num)
            if i > 0:
                lastRight = segments[i-1][2]
                response += s[lastRight+1:idxDigitStart]
                response += self.decode(s[left+1:right], num)
        response += s[right+1:]
        print("formString:", s, segments, "-->", response)
        return response        

    # Call separate to know whether we need to recurse down more
    # The end of recursion is also defined here
    # Handle the repeating number 
    def decode(self, s, num):
        print("decode:", num, "---", s)
        segments = self.separate(s)
        
        # No any brackets inside (end of recursion)
        if len(segments) == 0:
            ans = ""
            for i in range(num):
                ans += s
            print("seg=0 :", ans)
            print()
            return ans
        
        # Repeat the string num times
        oneText = self.formString(s, segments)
        response = ""
        for i in range(num):
            response += oneText
        return response

    # ================== Extract the parts with brackets ==================
    # This approach can only handle multi-layer brackets, but not multiple brackets in the same layer
    
#     def decodeString(self, s: str) -> str:
#         if len(s) == 0:
#             return s
#         return self.helper(s, 1) 
    
#     def helper(self, s, num):
#         print(num, s)
        
#         parts = []
#         leftIdx, rightIdx = 0, 0
#         while leftIdx != -1 :
#             try:
#                 leftIdx = s.index('[', rightIdx)
#                 rightIdx = s.index(']', leftIdx)
#                 parts.append((leftIdx, rightIdx))
#             except ValueError:
#                 leftIdx = -1
        
#         if len(parts) == 0:
#             ans = ""
#             for i in range(num):
#                 ans += s
#             return ans
        
#         for i in range(len(parts)):
#             rightIdx, leftIdx = parts[i][0], parts[i][1]
#             print(rightIdx, leftIdx)
#             nextNum = 0
#             nextStr = ""
#             alphaEndIdx = -1
#             for j in range(leftIdx, rightIdx+1):
#                 if s[j].isalpha():
#                     alphaEndIdx = j
#                     continue
#                 if s[j:leftIdx].isdigit():
#                     nextNum = int(s[j:leftIdx])
#                 nextStr = self.helper(s[leftIdx+1:rightIdx], nextNum)
#                 # print("alphaEndIdx:", alphaEndIdx)
#                 # print("nextStr:", nextStr)
#                 alphaEndIdx = rightIdx
#                 break
        
#             oneStr = s[:alphaEndIdx+1] + nextStr + s[rightIdx+1:]
#             ans = ""
#             for i in range(num):
#                 ans += oneStr
#             return ans
                
        