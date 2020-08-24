class Solution:
    
    # count the occurance [O(N + log(OCCURANCE)), 78%]
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = collections.Counter(nums)
        sortedKeys = sorted(count)
        ans = 0 
        for i in range(1, len(sortedKeys)):
            if sortedKeys[i] - sortedKeys[i-1] == 1:
                ans = max(ans, count[sortedKeys[i]] + count[sortedKeys[i-1]])
        return ans