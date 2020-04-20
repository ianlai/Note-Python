
# Two-level lists: size=1000000 [5%]
# Two-level lists: size=10000   [5%]
# Two-level lists: size=100     [5%]
    
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000000
        self.mp = [[]] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        if self.mp[idx]:
            for i in range(len(self.mp[idx])):
                if self.mp[idx][i][0] == key:
                    self.mp[idx][i][1] = value
                    return
            self.mp[idx].append([key, value])
        else:
            self.mp[idx].append([key, value])
            
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        if self.mp[idx]:
            for i in range(len(self.mp[idx])):
                if self.mp[idx][i][0] == key:
                    return self.mp[idx][i][1] 
            return -1
        else:
            return -1
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        if self.mp[idx]:
            for i in range(len(self.mp[idx])):
                if self.mp[idx][i][0] == key:
                    #self.mp[idx].pop(i)
                    del self.mp[idx][i]
                    break
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


#============================================
# Solution 
# Two-level lists [50%]
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

class MyHashMap1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

