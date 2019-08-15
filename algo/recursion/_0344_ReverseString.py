class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0, len(s)-1)
    def helper(self, s, right, left):
        if right >= left:
            return 
        self.helper(s, right+1, left-1)
        s[left], s[right] = s[right], s[left]
        # temp = s[left]
        # s[left] = s[right]
        # s[right] = temp

        