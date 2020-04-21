# hand = [1,2,3,6,2,3,4,7,8], W = 3
#
# 1: 1 
# 2: 1  1
# 3: 1  1
# 4:    1
# 6:       1
# 7:       1
# 8:       1

class Cards:
    def __init__(self, hand):
        self.mp  = {}
        for e in hand:
            self.mp[e] = self.mp.get(e, 0) + 1 
        self.arr = list(self.mp.keys())
        self.arr.sort()     
        self.cur = 0
        #print([list(x) for x in sorted(self.mp.items())])

    def hasNext(self):
        return self.cur < len(self.arr)
            
    def next(self):
        if self.hasNext():
            key = self.arr[self.cur]
            if key in self.mp:
                self.mp[key] -= 1
                if self.mp[key] == 0:
                    del self.mp[key]
            self.cur += 1 
            return key 
      
    def reset(self):
        for i in range(len(self.arr)):
            key = self.arr[i]
            if key in self.mp and self.mp[key] != 0:
                self.cur = i
                return
                
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if W <= 1:
            return True
        
        if len(hand) % W != 0:
            return False
        
        cards = Cards(hand)

        while cards.hasNext():
            prev = 0
            for i in range(W):
                if not cards.hasNext():
                    return False
                if i == 0:
                    prev = cards.next()
                    continue
                cur = cards.next()
                if prev != cur - 1:
                    return False
                prev = cur 
            cards.reset()
        return True
