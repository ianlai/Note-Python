from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        
        deq = deque([beginWord])
        visited = set()
        length_map  = {}
        for e in wordList:
            length_map[e] = 999
        length_map[beginWord] = 1
        max_length = 0
        while deq:
            cur = deq.popleft()
            # if used then skip it, otherwise add it to the set
            if cur in visited:
                continue
            visited.add(cur)
            # print("-------")
            # print("> " + cur)
            for word in wordList:
                if self.adjacentWords(cur, word):
                    if cur == word:
                        continue
                    
                    length_map[word] = min(length_map[cur]+1, length_map[word])
                    max_length = max(length_map[word], max_length)
#                     print(">>> " + word)
#                     print(length_map[cur], length_map[word], max_length)
                    
                    if word == endWord:
                        # print("end: " + endWord)
                        return max_length
                    deq.append(word)
        return 0
    
    def adjacentWords(self, s: str, e: str) -> bool:
        diff = 0
        for i in range(len(s)):
            if s[i] != e[i]:
                diff += 1
        if diff <=1:
            return True
        else:
            return False