class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):    
            num1, num2 = num2, num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        num3 = []
        
        # add num1 and num2 in the common length
        carry = 0
        for i in range(len(num2)):  #num2 is shorter
            sum = carry + int(num1[i]) + int(num2[i])
            carry = 0
            if sum >= 10:
                carry = 1
            sum %= 10
            num3.append(sum)
            
        # add remaining num1
        for i in range(len(num2), len(num1)):
            sum = carry + int(num1[i])
            carry = 0
            if sum >= 10:
                carry = 1
            sum %= 10
            num3.append(sum)
            
        # add remaining carry    
        if carry == 1:
            num3.append(1)
        
        ans = ''.join([str(x) for x in num3])
        ans = ans[::-1]
        return ans 