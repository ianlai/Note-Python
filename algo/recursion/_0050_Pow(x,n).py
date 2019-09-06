class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow_dict = {}
        return self.helper(x, n, pow_dict)
    def helper(self, x, n, pow_dict):
        # print(x, " ** ", n)
        # print(pow_dict)
        if n == 0:
            return 1
        if n > 0:
            half = int(n/2)
            
            if half not in pow_dict:
                    pow_dict[half] = self.helper(x, half, pow_dict)

            if n%2 == 0:
                return pow_dict[half] * pow_dict[half]
            else:
                return pow_dict[half] * pow_dict[half] * x
        if n < 0:
            half = int(n/2)
            
            if half not in pow_dict:
                    pow_dict[half] = self.helper(x, half, pow_dict)
                
            if n%2 == 0:
                return pow_dict[half] * pow_dict[half]
            else:
                return pow_dict[half] * pow_dict[half] / x
    
        
    def myPowNaive(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            return self.myPow(x, n-1) * x
        if n < 0:
            return self.myPow(x, n+1) / x
        
        