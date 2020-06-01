class Solution:
    
    # stack [O(n1), 43%-66%]
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        stack = [(T[0], 0)] #value, index
        ans = [0] * len(T)
        for i in range(1, len(T)):
            while stack and T[i] > stack[-1][0]:  #pop out until new element smaller than the last one in stack 
                removed = stack.pop()
                ans[removed[1]] = i - removed[1] 
            stack.append((T[i], i))               #push in to the stack
        return ans
    
    # =====================================================
    
    # 2-layer loops: [O(n2), TLE]
    def dailyTemperatures1(self, T: List[int]) -> List[int]:
        if not T:
            return []
        ans = []
        for i in range(len(T)):
            cur = T[i]
            diff = 1
            for j in range(i+1, len(T)):
                if T[j] > cur:
                    ans.append(diff)
                    break
                diff += 1
            if diff == len(T) - i:
                ans.append(0)
        return ans