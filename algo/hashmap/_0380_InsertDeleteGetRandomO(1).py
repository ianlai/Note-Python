class RandomizedSet:
    is_debug = False
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            self.debug("Insert: " + str(val))
            return False
        else:
            size = len(self.map)
            self.map[val] = size  #add in map (new index)
            self.arr.append(val)  #add in arr
            self.debug("Insert: " + str(val))
            return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.map:
            size = len(self.map)
            index = self.map[val]
            last  = self.arr[-1]
            
            self.arr[index] = last  #del from arr (move last to index, arr)
            self.map[last] = index  #del from arr (move last to index, map)
            self.arr.pop()          #del from arr (remove the last)
            del self.map[val]       #del from map (this line needs to be run in last, otherwise self.map[last] might add one element back)
            
            self.debug("Remove: " + str(val))
            return True
        else:
            self.debug("Remove: " + str(val))
            return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        size = len(self.map)
        rand = random.randint(0, size-1)
        self.debug("getRandom: " + str(self.arr[rand]))
        return self.arr[rand]
    
    def debug(self, msg):
        if RandomizedSet.is_debug is False:
            return 
        print(msg)
        print(">> ", self.arr)
        print(">> ", self.map)
        print("--------------")

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()