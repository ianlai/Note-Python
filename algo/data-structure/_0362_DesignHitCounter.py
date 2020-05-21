# Dictionary to store the counts 
class HitCounter:

    # hit: O(1), getHits: O(n) [54%]  //remove the staled pairs on the fly
    # hit: O(1), getHits: O(n) [6%]   //just skip the staled pairs
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = {}
        
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp in self.count:
            self.count[timestamp] += 1
        else:
            self.count[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for k in list(self.count.keys()):   #need to convert it to list so that we can delete the staled ones
            if k > timestamp - 300:
                res += self.count[k]
            else:
                del self.count[k]
        return res

# ==============================================================

# Deque to store the timestamps
class HitCounter1:

    # hit: O(1), getHits: O(n) [15%]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = collections.deque([])
        self.validSeconds = 5 * 60 
        
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.count.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        lastValidTime = timestamp - self.validSeconds
        while self.count and self.count[0] <= lastValidTime:
            self.count.popleft()
        return len(self.count)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)