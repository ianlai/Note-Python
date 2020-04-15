class Solution:
        
    # Traverse once [O(n), 75%]
    # -> next start is from the station next to the failed station 
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [g - c for g, c in zip(gas, cost)]
        #print(diffs)
        run, i = 0, 0 
        while run < len(diffs):
            #print(i)
            if diffs[i] < 0:
                run += 1
                i = (i + 1) % len(diffs)
                continue
            count = 0
            rest = 0
            for d in range(len(diffs)):
                j = (i + d) % len(diffs)
                #print(i, j, d)
                rest += diffs[j]
                if rest >= 0: #
                    count += 1
                else:
                    count = 0 
                    i = (j + 1) % len(diffs)
                    break
            if count == len(diffs):
                return i
            run += 1 
        return -1    
            
    # Naive approach [O(n2), 5%]
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        diffs = [g - c for g, c in zip(gas, cost)]
        print(diffs)
        for i in range(len(diffs)):
            if diffs[i] < 0:
                continue
            count = 0
            rest = 0
            for d in range(len(diffs)):
                j = (i + d) % len(diffs)
                rest += diffs[j]
                if rest >= 0: #
                    count += 1
            if count == len(diffs):
                return i
        return -1    