class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for e in s: 
            if e == '(' or e == '[' or e == '{':
                stack.append(e)
            else:
                if stack:
                    pop = stack.pop()
                else:
                    return False   #']'
                if pop == '(' and e == ')': 
                    continue 
                if pop == '[' and e == ']': 
                    continue 
                if pop == '{' and e == '}': 
                    continue 
                return False #invalid
        if stack:
            return False 
        else:
            return True
            