class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        ansArr = []
        self.backtracking(candidates, target, ansArr, [], 0)
        return ansArr
        
    def backtracking(self, candidates, target, ansArr, curArr, index):
        if target < 0:
            #print(candidates[index], " x", curArr)
            return 
        if target == 0:
            #print(candidates[index], " o", curArr)
            ansArr.append(curArr)
            return 
        if target > 0:
            #print(candidates[index], " ?", curArr)
            for i in range(index, len(candidates)):
                
#                 ### (wrong) Append then remove (the change of the curArr in recursion will be kept)
#                 curArr.append(candidates[i])
#                 self.backtracking(candidates, target-candidates[i], ansArr, curArr, i)
#                 curArr = curArr[:len(curArr)-1]
                
#                 ### (correct) Append then remove (the change of the curArr in recursion will NOT be kept)
#                 curArr.append(candidates[i])
#                 self.backtracking(candidates, target-candidates[i], ansArr, curArr.copy(), i)
#                 curArr = curArr[:len(curArr)-1]
                
                ### (correct) Pass a new array 
                self.backtracking(candidates, target-candidates[i], ansArr, curArr+[candidates[i]], i)
                
            return