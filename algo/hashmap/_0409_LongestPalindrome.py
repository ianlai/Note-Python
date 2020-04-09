class Solution(object):
    
    # Use Counter
    def longestPalindrome(self, s):
        cnt = collections.Counter(s)
        count = 0
        for e in cnt: 
            if cnt[e] % 2 == 0:
                count += cnt[e] 
            else:
                count += cnt[e] - 1 
                
        if count == len(s):
            return count 
        else:
            return count + 1
    
    #=================================
    
    # Use set 
    def longestPalindrome1(self, s):
        if not s:
            return 0
        
        char_set = set()
        longest_count = 0
        
        for char in s:
            if char not in char_set: 
                char_set.add(char)
            else:
                char_set.remove(char)
                longest_count += 2
                
        #put a single char into the center of pairs 
        if len(char_set) > 0:
            longest_count +=1 
            
        return longest_count 