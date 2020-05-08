class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if len(cells) == 0:
            return []
        
        temp = [-1] * len(cells) 
        #pToNext = {}
        pToIdx = {}
        idxToP = {}
        if N == 0:
            return cells
        
        for i in range(N):
            #print(i, cells)
            
            if tuple(cells) in pToIdx:
                repeatFirst = pToIdx[tuple(cells)] 
                repeatSecond = i 

                ### Another idea to use map to accelerate, but actually it won't help (TLE)
                # cells = pToNext[tuple(cells)] 
                
                ### Find the repetition and find the answer in the repetition group 
                repeatInterval = repeatSecond - repeatFirst
                print("repeatInterval:", repeatInterval)
                
                # Shift N back to the first group or before the first group
                N %= repeatInterval
                
                # Calibrate into the first group 
                if N < repeatFirst:
                    N += repeatInterval

                return idxToP[N]
                
                
            for j in range(1, len(cells)-1, 1):
                temp[0], temp[-1] = 0, 0
                if cells[j-1] == cells[j+1]:
                    temp[j] = 1
                else:
                    temp[j] = 0
            
            pToIdx[tuple(cells)] = i
            idxToP[i] = cells
            #pToNext[tuple(cells)] = tuple(temp)
            cells = temp[:]
            
        return cells