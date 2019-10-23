class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms is None or len(rooms) == 0:
            return True
        keys = set()   #avoid redundance
        keys.update(rooms[0])
        opened = set([0])
        visited = [0] * len(rooms)
        
        # we use keys as a stack, so this is a DFS 
        # if we use a queue, then it will be a BFS
        while keys:
            curKey = keys.pop()        #pick out a key from our keys
            if visited[curKey] == 1:   #skip the room we have checked
                continue
            print(curKey, keys)
            opened.add(curKey)      #open a room
            visited[curKey] = 1        #mark the room
            keys.update(rooms[curKey]) #get the keys in the room 
        
        #print(opened)
        if len(rooms) == len(opened):
            return True
        return False
        
        
        