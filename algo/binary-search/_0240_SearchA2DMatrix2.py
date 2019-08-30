class Solution:
    def searchMatrix(self, mat, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if mat is None or len(mat) == 0 or len(mat[0]) == 0:
            return False
        
        m = len(mat)
        n = len(mat[0])
        
        idxCol = 0 
        idxRow = n-1
    
        while True:
            if mat[idxCol][idxRow] == target:
                return True
            if mat[idxCol][idxRow] < target:
                if idxCol == m-1:
                    return False
                else:                
                    idxCol += 1
            if mat[idxCol][idxRow] > target:
                if idxRow == 0:
                    return False
                else:
                    idxRow -= 1
                
        if mat[idxCol][idxRow] == target:
            return True
        else: 
            return False