class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.arr = [-1] * self.size  

    def add(self, key: int) -> None:
        # print("add:", key)
        index = key % self.size 
        if self.arr[index] == -1:
            self.arr[index] = [key]
        else:
            if key in self.arr[index]: 
                return 
            else:
                self.arr[index].append(key)
        # print(self.arr)
        # print("----------")

    def remove(self, key: int) -> None:
        # print("remove:", key)
        index = key % self.size 
        if self.arr[index] != -1 and key in self.arr[index]:
            self.arr[index].remove(key) 
        # print(self.arr)
        # print("----------")
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        # print("contains:", key)
        # print(self.arr)
        # print("----------")
        index = key % self.size
        if self.arr[index] == -1:
            return False
        else:
            if key in self.arr[index]:
                return True
            else:
                return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)