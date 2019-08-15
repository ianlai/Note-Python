from collections import deque
class Solution:
    def ladderLength333(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        #wordList.append(endWord)
        deq = deque([beginWord])
        visited = set()
        
        distance = 0
        while deq:
            distance += 1
            # Pop all for this layer (range will be fixed once entering)
            #print(distance)
            for _ in range(len(deq)):  
                cur = deq.popleft()
                print(cur)
                adjacents = self.get_adjacent_words(cur) 
                if cur == endWord:
                        print(">>>>> ", word, " ", str(distance))
                        return distance

                # loop the possible adjacents
                for word in adjacents: 
                    
                    if word in wordList and word not in visited:
                        #print(">> ", word)
                        deq.append(word)
                        visited.add(word)
        return 0
    
    def ladderLength(self, start, end, wordList):
        wordList.append(end)
        queue = collections.deque([start])
        visited = set([start])
        
        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
                
                for next_word in self.get_adjacent_words(word):
                    if next_word not in wordList or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word) 

        return 0
    
    def get_adjacent_words(self, s: str) -> bool:
        adjacents = []
        for i in range(len(s)):
            left  = s[:i]
            right = s[i+1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char == s[i]:
                    continue
                adjacents.append(left+char+right)
        return adjacents
            