class Solution:
    def __init__(self):
        self.size = 10
        self.idxToHour = {
            1: 8,
            2: 4,
            3: 2,
            4: 1
        }
        self.idxToMin = {
            5: 32,
            6: 16,
            7:  8,
            8:  4,
            9:  2,
            10: 1
        }
    
    #Combination with Transformation 
    def readBinaryWatch(self, num: int) -> List[str]:
        if num == 0:
            return ["0:00"]
        ans = []
        self.dfs(num, ans, [], 1)
        return ans
    
    def dfs(self, num, ans, cur, idx):
        if len(cur) == num:
            timeString = self.transform(cur)
            if timeString:
                ans.append(timeString)
        
        for i in range(idx, self.size + 1):
            self.dfs(num, ans, cur + [i], i + 1)    
        
    def transform(self, cur: List[int]) -> str:
            hours = 0
            mins = 0
            for e in cur:
                if e <= 4:  #hour
                    hours += self.idxToHour[e]
                if e >= 5:  #min
                    mins += self.idxToMin[e]
            timeString = ""
            if hours > 11: 
                return None
            if mins > 59: 
                return None 
            if mins < 10: 
                timeString = str(hours) + ":" + "0" + str(mins)
            else:
                timeString = str(hours) + ":" + str(mins)
            return timeString
            
            