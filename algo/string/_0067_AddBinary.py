class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = a[::-1]
        b = b[::-1]
        
        # a > b
        if len(a) < len(b):
            a, b = b, a
        
        ans = []
        carry = 0
        for i in range(len(a)):
            inta, intb, cur = 0, 0, 0 
            if i >= len(b):
                inta, intb = int(a[i]), 0
            else:
                inta, intb = int(a[i]), int(b[i])
                
            total = inta + intb + carry
            
            if total == 0:
                cur, carry = 0, 0
            elif total == 1:
                cur, carry = 1, 0 
            elif total == 2:
                cur, carry = 0, 1
            else:
                cur, carry = 1, 1
    
            ans.append(cur)
        if carry == 1:
            ans.append(carry)
        ans = ans[::-1]
        return ''.join([str(x) for x in ans])