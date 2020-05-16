class Solution:

    # TODO: Refactor [8%]
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return True
        
        stack = []
        n = len(pushed)
        
        j = 0 
        for i in range(n):
            cur = popped[i]
            #print("popped[", i,"]:", cur)
                
            while True:
                if j == n:
                    #print("  j==n")
                    if not stack:
                        return True
                    if stack and stack.pop() == cur:
                        break
                    else: 
                        return False
                else: # j < n
                    #print("  pushed[", j,"]:", pushed[j])
                    if stack and stack[-1] == cur:
                        stack.pop()
                        break
                    stack.append(pushed[j])
                    j += 1
                    
                if stack and stack[-1] == cur:
                    stack.pop()
                    break
            #print(stack, j)
                
        return True