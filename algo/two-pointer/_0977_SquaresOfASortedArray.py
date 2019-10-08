class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if A is None or len(A)==0:
            return None
        if len(A) == 1:
            return [A[0] ** 2]
            
        min = A[0]
        minIdx = 0 
        
        for i in range(len(A)):
            if abs(A[i]) < abs(min):
                min = A[i]
                minIdx = i
        
        left, right = minIdx, minIdx
        if minIdx == len(A) - 1:
            left = minIdx - 1
        else:
            right = minIdx + 1

        print(left, ": ", A[left])
        print(right, ": ", A[right])
        ans = []
        
        while True:
            if left >= 0 and right <= len(A) - 1:
                if abs(A[left]) <= abs(A[right]):
                    ans.append(A[left] ** 2)
                    left -= 1
                elif abs(A[left]) > abs(A[right]):
                    ans.append(A[right] ** 2)
                    right += 1
            elif left >= 0 and right > len(A) - 1:
                ans.append(A[left] ** 2)
                left -= 1
            elif left < 0 and right <= len(A) - 1:
                ans.append(A[right] ** 2)
                right += 1
            else:
                break 
                
        return ans