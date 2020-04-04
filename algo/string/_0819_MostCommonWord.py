class Solution:
    
    
    # Faster: replace punctuation with space (not empty string) -> split with space (remove space)  (89%)
    # Since we do "split with space" to remove the space anyway, we don't need to run the "split with punctuation"
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = []
        countMap = {}
        punctuations = ['!', '\'', '?', ',', ';', '.'] 
        
        # (1) Convert all alphabets to lowercase (call together, not separatly)
        paragraph = paragraph.lower()
        
        # (2) Replace punctuations with space 
        for punctuation in punctuations: 
            paragraph = paragraph.replace(punctuation,' ')
        
        # (3) Split with white space
        words = paragraph.split()
        
        for word in words:           
            if word in banned:  #the speed if using list and set are not that different @@? 
                continue
                
            # (4) Make the count map
            countMap[word] = countMap.get(word, 0) + 1
                
        
        maxOccurance = 0 
        maxOccuranceWord = ""
        for word in countMap:
            if countMap[word] > maxOccurance:
                maxOccurance = countMap[word]
                maxOccuranceWord = word
    
        return maxOccuranceWord
    
    # ==================================================
    
    # Slow: split with space -> split with comma -> replace punctuation with empty string (7%)
    def mostCommonWord1(self, paragraph: str, banned: List[str]) -> str:
        words = []
        
        # Split with white space
        needProcessWords = paragraph.split()
        
        # Split with comma in each split word
        for word in needProcessWords:
            words.extend(filter(None, word.split(',')))
        
    
        punctuations = ['!', '\'', '?', ',', ';', '.'] 
        
        bannedSet = set()
        countMap = {}
        for word in banned: 
            bannedSet.add(word)
        
        for word in words: 
            word = word.lower()
            
            for punctuation in punctuations: 
                word = word.replace(punctuation,'')
            print(word)
            
            if word in banned: #the speed if using list and set are not that different @@? 
                continue
                
            # Clearer to count with a map
            countMap[word] = countMap.get(word, 0) + 1
                
            # if word in countMap:
            #     countMap[word] += 1
            # else:
            #     countMap[word] = 1
        
        maxOccurance = 0 
        maxOccuranceWord = ""
        for word in countMap:
            if countMap[word] > maxOccurance:
                maxOccurance = countMap[word]
                maxOccuranceWord = word
    
        return maxOccuranceWord