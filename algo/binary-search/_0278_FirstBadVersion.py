# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n 
        while start + 1 < end:
            mid = int((start + end)/2)
            if isBadVersion(mid-1) == False and isBadVersion(mid) == True:
                return mid
            elif isBadVersion(mid-1) == False and isBadVersion(mid) == False:
                start = mid
            elif isBadVersion(mid-1) == True and isBadVersion(mid) == True:
                end = mid 
        #Last one 
        if isBadVersion(start) == False and isBadVersion(end) == True:
            return end
        #First one
        if isBadVersion(start) == True:
            return start