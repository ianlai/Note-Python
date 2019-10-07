class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers is None or len(numbers) == 0:
            return None
        
        start, end = 0, len(numbers) - 1
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start+1, end+1]
            elif sum > target:
                end -= 1
            else: 
                start += 1
        return None
        