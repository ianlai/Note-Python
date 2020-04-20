class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        if not items:
            return []
        
        mp = {}
        ans = []
        for s in items:
            if s[0] in mp:
                mp[s[0]].append(s[1])
            else:
                mp[s[0]] = []
                mp[s[0]].append(s[1])
        #print(mp)
        
        for studentId in mp:
            studentScores = sorted(mp[studentId], reverse = True)
            studentAvg = sum(studentScores[:5]) // 5
            ans.append([studentId, studentAvg])
            
        return ans