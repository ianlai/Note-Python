class Solution:

    # DP [O(n)]  (83%)
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        
        f = [0] * (num + 1)
        f[0], f[1] = 0, 1
        curPowerTwo, nextPowerTwo = 2, 2 
        for n in range(2, num+1): 
            if n == nextPowerTwo:
                curPowerTwo = nextPowerTwo
                nextPowerTwo = nextPowerTwo * 2
            #print(n, "->", n-curPowerTwo)
            f[n] = f[n - curPowerTwo] + 1
        return f
    
    # Naive approach: traverse + loop to shift bits [O(n * bit of n)] (6%)
    def countBits1(self, num: int) -> List[int]:
        count = []
        for n in range(num+1): 
            cnt = 0
            while n != 0:
                if n & 1 == 1:
                    cnt += 1
                n >>= 1
            count.append(cnt)
        return count
                