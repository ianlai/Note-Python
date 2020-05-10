class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if len(s) == 0:
            return s
        if len(shift) == 0:
            return s
        
        leftShift = 0
        for i in range(len(shift)):
            if shift[i][0] == 0:
                leftShift += shift[i][1]
            else:
                leftShift -= shift[i][1]
        print(leftShift)
        if leftShift == 0:
            return s
        elif leftShift > 0:
            while leftShift >= len(s):
                leftShift -= len(s)
            return s[leftShift:] + s[:leftShift]
        else:
            while abs(leftShift) >= len(s):
                leftShift += len(s)
            leftShift = len(s) - abs(leftShift)
            return s[leftShift:] + s[:leftShift]
            