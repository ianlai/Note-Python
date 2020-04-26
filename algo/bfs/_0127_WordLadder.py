from collections import deque
class Solution:
    
    # BFS, with searching possibitilties, with changing wordList to set [O(NL^2), 20%]
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # Search the possibilities: [faster, O(25L^2)]
        def getNextWords(word):
            neighbors = []
            alphabets = "abcdefghijklmnopqrstuvwxyz"
            for i in range(len(word)):
                for char in alphabets:
                    neighbors.append(word[:i] + char + word[i+1:])
            return neighbors  #The elements inside are not necessary in wordList
            
            
        # Search for the wordList: [slow, O(NL)]
        def getNextWords2(word):
            neighbors = [] 
            for candidate in wordList:
                diff = 0
                for i in range(len(word)):
                    if word[i] != candidate[i]:
                        diff += 1
                if diff == 1:
                    neighbors.append(candidate)
            return neighbors
            
        dq = deque([beginWord])
        visited = set([beginWord])
        distance = {beginWord: 1}
        
        wordList = set(wordList)  #TLE if we don't change wordList to a set 
        
        while dq:
            word = dq.popleft()
            for nextWord in getNextWords(word): 
                if nextWord in visited or nextWord not in wordList: #check whether it is in wordList 
                    continue
                if nextWord == endWord:
                    return distance[word] + 1
                distance[nextWord] = distance[word] + 1
                dq.append(nextWord)
                visited.add(nextWord)
        return 0 