class Solution:
    
    # Sort and then traverse [O(nlogn), 7%]
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        
        n = len(citations)
        hIndex = n 
        
        for i in range(len(citations)):
            if citations[i] < hIndex:
                hIndex -= 1
            else:
                break
        
        return hIndex 