class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        #squareList = [i*i for i in range(x+1)] 
        start, end = 0, x 
        while start + 1 < end: 
            mid = (start + end) //2
            if mid**2 <= x < (mid+1)**2:
                return mid
            if x < mid**2:
                end = mid
            if x >= (mid+1)**2:
                start = mid 
        