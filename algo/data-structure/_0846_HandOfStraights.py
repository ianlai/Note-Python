# hand = [1,2,3,6,2,3,4,7,8], W = 3
#
# 1: 1 
# 2: 1  1
# 3: 1  1
# 4:    1
# 6:      1
# 7:      1
# 8:      1


# Define a data structure to handle the next item [5%]
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
                
class Solution1:
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

#=============================================

# Sort map then transform to list of list [15%]
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:    
        # special case 
        if W <= 1:
            return True
        if len(hand) % W != 0:
            return False
        
        mp = {}
        ans = []
        
        # count the elements
        for e in hand:
            mp[e] = mp.get(e, 0) + 1
        
        # sort the map and transform to list of list
        cards = [list(x) for x in sorted(mp.items())]
        print(cards)
        
        while cards:
            cur = cards[0][0]
            # loop the start value to start value + W (not W elements)
            for val in range(cur, cur + W):
                idx = self.contains(cards, val) 
                if idx != -1:
                    cards[idx][1] -= 1
                    if cards[idx][1] == 0:
                        cards.pop(idx)
                else:
                    return False
        return True
    
    # since cards is a list, we need to traverse to check whether it contains val 
    # this part should be improved  
    def contains(self, cards, val):
        for i in range(len(cards)):
            if cards[i][0] == val:
                return i
        return -1
    
        