
# Map with binary search to insert and get [7%]
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            arr = self.mp[key]
            tup = (timestamp, value)
            
            # Binary Search
            idx = self.binarySearch(arr, timestamp)
            if idx == -1:
                arr.append(tup)
            if arr[idx][0] == timestamp:
                arr[idx] = value
            else: 
                arr.insert(idx+1, tup)  # Linear insert (linkedlist can solve this)
            
            # Linear Search 
            # if timestamp > arr[-1][0]:
            #     arr.append((timestamp, value))
            # for i in range(1, len(arr)):
            #     if arr[i-1][0] == timestamp:
            #         arr[i-1] = (timestamp, value)
            #         break
            #     if arr[i-1][0] < timestamp < arr[i][0]:
            #         arr.insert(i, (timestamp, value))
            #         break
        else:
            self.mp[key] = []
            self.mp[key].append((timestamp, value))      
        #print("set:", key, self.mp)
            
    def get(self, key: str, timestamp: int) -> str:
        #print("get:", key, self.mp)
        if key in self.mp:
            arr = self.mp[key]

            # Binary Search
            idx = self.binarySearch(arr, timestamp)
            if idx == -1:
                return ""
            return arr[idx][1]

            # Linear Search
            # if timestamp < arr[0][0]:
            #     return ""
            # if timestamp == arr[0][0]:
            #     return arr[0][1]
            # if timestamp >= arr[-1][0]:
            #     return arr[-1][1]
            # for i in range(len(arr)-1, 0, -1):
            #     if timestamp < arr[i][0]:
            #         return arr[i-1][1]
        else:
            return ""
    # Find an interval which arr[i-1][0] <= timestamp < arr[i][0]
    # Return arr[i-1][1]
    def binarySearch(self, arr, timestamp):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if timestamp < arr[mid][0]:
                end = mid 
            elif timestamp == arr[mid][0]:
                return mid
            else:
                start = mid
                
        if timestamp < arr[start][0]:
            return -1
        elif timestamp >= arr[start][0] and timestamp < arr[end][0]:
            return start
        return end
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)