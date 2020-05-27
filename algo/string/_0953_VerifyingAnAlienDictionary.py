class Solution:
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # if wordA < wordB 
        def compare(wordA, wordB):
            #print("compare:", wordA, wordB)
            for i in range(len(wordA)):
                if i >= len(wordB):
                    return False  
                A, B = wordA[i], wordB[i]
                #print(A, B, cToI[A], cToI[B])
                if cToI[A] < cToI[B]:
                    return True
                elif cToI[A] > cToI[B]:
                    return False
            return True
        if len(words) == 0:
            return True
        cToI = {}
        for i, e in enumerate(order):
            cToI[e] = i
        
        for i in range(1, len(words)):
            if not compare(words[i-1], words[i]):
                return False
        return True
            
        