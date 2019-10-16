class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        
        start, end = 1, num
        
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num: 
                start = mid 
            else:
                end = mid 
        
        if start * start == num:
            return True
        if end * end == num:
            return True
        
        return False
            