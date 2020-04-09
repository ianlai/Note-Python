class Solution:
    
    # DFS (backtracking) 
    # Implicit Graph: What I can select for the next?
    # 
    # Ex. [1,2,3]
    # [1] - [1,2] - [1,2,3]
    #     |       - [1,2]
    #     - [1]   - [1,3]
    #             - [1]
    # [x] - [2]   - [2,3]
    #     |       - [2]
    #     - [x]   - [3]
    #             - [x]
    #
    # Adding point: Each leaf
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, cur, index, ans):
            ans.append(cur)
            for i in range(index, len(nums)):
                dfs(nums, cur + [nums[i]], i + 1, ans)
            
        if not nums or len(nums) == 0:
            return []

        ans = []
        dfs(nums, [], 0, ans)
        return ans

    # ======================================================
    # DFS 
    # Implicit Graph: Whether I should select the next? 
    # 
    # Ex. [1,2,3]
    # [x] - [1]  - [1,2] - [1,2,3]
    #     |      - [1,3]
    #     - [2]  - [2,3]
    #     |
    #     - [3]
    #
    # Adding point: Each node
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, ans, curArr, index):
            if index == len(nums):
                ans.append(curArr)
                return
            dfs(nums, ans, curArr+[nums[index]], index+1)
            dfs(nums, ans, curArr, index+1)
            return

        if not nums:
            return []
        ans = []
        dfs(nums, ans, [], 0)
        return ans
    # ======================================================
    # Double
    def subsets_double(self, nums: List[int]) -> List[List[int]]:
        print("3")
        if not nums:
            return []
        ansArr = []
        ansArr.append([])
        ansArr.append([nums[0]])
        print(ansArr)
        for i in range(1, len(nums)):
            #newArr = ansArr[:]  #new list (but only 1 layer)
            newArr = [cur[:] for cur in ansArr] #new list
            #print("newArr:", newArr)
            for cur in newArr:
                cur.append(nums[i])
            ansArr.extend(newArr)
            #print("ansArr:", ansArr)
        return ansArr