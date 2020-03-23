import heapq
import collections

class Solution:
    
    # Use Counter and sorted() (sort all, should be slower)
    def topKFrequent_sorted(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)              #count
        sortedCnt = sorted(cnt.items(), key=lambda kv: kv[1], reverse=True) #sort by value (map)
        sortedCntCount = [kv[0] for kv in sortedCnt]      #sorted list by occurance 
        ans = sortedCntCount[:k]                          #top-k 
        return ans
    
    # Use Counter and heapq.nlargest
    def topKFrequent_nlargest(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)              #count
        ans = heapq.nlargest(k, cnt, cnt.get)        #top-k
        return ans
    
    # Use Counter and most_common function 
    def topKFrequent_most_common(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)              #count   
        ans = [ kv[0] for kv in cnt.most_common(k) ] #top-k
        return ans
        
        
    # Use primitive structures  
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return None
        
        numToCount = {}
        countToNum = {}
        countHeap = []
        ans = []
        
        # Step1: Count the nums and put in numToCount{int: int} 
        for e in nums:
            if e in numToCount:
                numToCount[e] += 1
            else:
                numToCount[e] = 1
        print("numToCount:", numToCount)
        
        # Step2: Form the countToNum{int: List[int]} 
        for num in numToCount:
            count = numToCount[num]
            if count in countToNum:
                countToNum[count].append(num)
            else:
                countToNum[count] = []
                countToNum[count].append(num)
        print("countToNum:", countToNum)
        
        # Step3: Sort the countToNum with key, and the arrays need to be moved together
        #countToNumSorted = sorted(countToNum)  #sort the key (wrong, only key list left)
        countToNumSorted = sorted(countToNum.items(), key=lambda kv: kv[0], reverse=True)  #sort the key
        print("countToNum (sorted):", countToNumSorted)
        
        # Step4: Form the ans list by pulling out the list from countToNumSorted{} (extend the whole list)
        for countToNumTuple in countToNumSorted:
            numArr = countToNumTuple[1]
            if len(numArr) < k: 
                ans.extend(numArr)
                k -= len(numArr)
            else:
                break

        # Step5: Form the ans list by adding the last few numbers (extend the partial list)
        for i in range(k): 
            ans.append(numArr[i])
        
        return ans
        