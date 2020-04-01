class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        
        digits = []
        nums = set([n])
        print(n)
        
        count = 0
        while n != 1:
            
            # Separate digits
            while n >= 10 :
                r = n % 10
                n //= 10
                digits.append(r)
            digits.append(n)
            #print(nums)
            
            # Make the next n 
            n = 0
            for e in digits:
                n += e**2
            #print(n)
            if n in nums:
                return False
            nums.add(n)
            digits = []
        return True
            