class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        arr = []
        while x > 0:
            arr.append(x % 10)
            x = x // 10

        p1, p2 = 0, len(arr) - 1
        while p1 < p2:
            if arr[p1] != arr[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True