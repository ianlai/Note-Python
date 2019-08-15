class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        if tiles is None: 
            return 0
        if tiles == "":
            return 0
        tiles = ''.join(sorted(tiles))  #sort the string 
        countDict = {}
        #print(tiles)
        
        #count the chars 
        for e in tiles:
            if e in countDict:
                countDict[e] += 1
            else:
                countDict[e] = 1    
        #print(countDict)
                
        #print(countDict)
        ans = [0]  #use ans[0] to record the answer
        self.dfs(countDict, ans) 
        return ans[0]
    
    def dfs(self, countDict, ans):
        # check
        # dictSum = 0
        # for e in countDict:
        #    dictSum += countDict[e]
        # if dictSum == 0:
        #     return 0
        
        levelSum = 0
        for e in countDict:
            if countDict[e] > 0:
                #print(countDict, ans[0])
                ans[0] += 1         #cur level
                countDict[e] -= 1 
                levelSum = self.dfs(countDict, ans) 
                ans[0] += levelSum  #sub level
                countDict[e] += 1 
            #else:
                #print(countDict, ans[0], "xx")
                    
        return levelSum 
        
        