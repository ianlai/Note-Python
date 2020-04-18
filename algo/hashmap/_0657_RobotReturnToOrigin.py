class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = collections.Counter(moves)
        if cnt['U'] != cnt['D']:
            return False
        if cnt['L'] != cnt['R']:
            return False
        return True
            