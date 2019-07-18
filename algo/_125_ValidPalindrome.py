class Solution(object):
    def isPalindrome(self, s):
        length = len(s)
        s=s.lower()  # s.lower() won't work
        i=0
        j=length-1
        while i <= j < length:
            while i <= j < length and s[i].isalpha() != True and s[i].isdigit() != True : 
                i = i + 1
            while i <= j < length and s[j].isalpha() != True and s[j].isdigit() != True :  
                j = j - 1
            if not i <= j < length:
                return True
            if s[i] == s[j]: 
                i = i + 1
                j = j - 1
            else:
                return False
        return True


obj = Solution()
            
print(obj.isPalindrome("abcba"))                           #True
print(obj.isPalindrome("123321"))                          #True
print(obj.isPalindrome("987889"))                          #False
print(obj.isPalindrome("AAAbbbccBBBaaa"))                  #True
print(obj.isPalindrome("a , b,b  a"))                      #True
print(obj.isPalindrome("race a car"))                      #False
print(obj.isPalindrome(" "))                               #True
print(obj.isPalindrome("   a"))                            #True
print(obj.isPalindrome("A man, a plan, a canal: Panama"))  #True
print(obj.isPalindrome("9M"))                              #False
