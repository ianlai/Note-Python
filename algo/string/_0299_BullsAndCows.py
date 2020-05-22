class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        A = 0
        B = 0
        
        count = collections.Counter(secret)
        
        #Calculate A
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                count[guess[i]] -= 1
                A += 1
                
        #Calculate B    
        for i in range(len(guess)):
            if guess[i] != secret[i]:
                if guess[i] in count and count[guess[i]] > 0:
                    B += 1
                    count[guess[i]] -= 1
                
        return str(A) + "A" + str(B) + "B" 