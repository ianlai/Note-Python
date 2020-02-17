class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.mp:
            self.mp[number] += 1 
        else:
            self.mp[number] = 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for e in self.mp:
            if e == value - e: 
                if self.mp[e] == 1: 
                    continue       #special case: [2], [4] -> False
                else:
                    return True    #normal case : [2,2], [4] -> True
            else:
                if value - e in self.mp:
                    return True
                else:
                    continue
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)