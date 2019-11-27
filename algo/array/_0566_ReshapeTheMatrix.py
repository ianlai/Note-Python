class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return None
        #print("r=", r, "c=", c)
        
        m = len(nums)
        n = len(nums[0])

        if m * n != r * c:
            return nums
        
        ans = []
        count = 0
        for i in range(m):
            for j in range(n):
                row = count // c
                col = count % c
                if col == 0:
                    ans.append([])
                ans[row].append(nums[i][j])
                count += 1
        
        #print(ans)
        return ans