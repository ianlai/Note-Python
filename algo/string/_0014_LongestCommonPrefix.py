class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        idx = 0
        ans = []
        while True: 
            cur = ""   #current char 
            for j in range(len(strs)):
                if idx == len(strs[j]):
                    return ''.join(ans)
                
                if cur == "":
                    cur = strs[j][idx]
                    continue
                if cur != strs[j][idx]:
                    return ''.join(ans)
            ans.append(strs[0][idx])
            idx += 1
        return ''.join(ans)