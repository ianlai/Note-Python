import heapq

class Solution():
    
    # Use heap; each element in heap is a tuple (val, idx, prime)  (82%)
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n <= 0 or not primes: 
            return -1
        
        heap = []
        ansset = set([1])
        anslist = [1]
        # insert the first part 
        for i in range(len(primes)):
            heapq.heappush(heap, (primes[i], 0, primes[i]))  #val(variable), idx, primes(static)
        
        # add point one by one, not list by list 
        while len(anslist) < n:
            #print("heap:", heap, " | anslist:", anslist)
            cur, idx, prime = heap[0]  #peek 
            if cur not in ansset:      #avoid redandunt (output)
                ansset.add(cur)  
                anslist.append(cur) 
            nxt = (prime * anslist[idx+1], idx + 1, prime)
            heapq.heappush(heap, nxt)
            cur, idx, prime = heapq.heappop(heap)
            
        return anslist[n-1]
    
    # Use heap; each element in heap is val; use set to remove the redandunts (TLE)
    def nthSuperUglyNumber_1(self, n: int, primes: List[int]) -> int:
        if n <= 0 or not primes: 
            return -1
        
        heap = [e for e in primes] #deep copy
        heapq.heapify(heap)
        hset = set(heap) 
        ansset = set([1])
        anslist = [1]
        
        # add list by list (each time one list will be added)
        while len(anslist) < n:
            #print("heap:", heap, " anslist:", anslist)
            cur = heap[0]  #peek 
            for e in primes: 
                nxt = cur * e 
                if nxt not in heap:  #avoid redandunt (input)
                    heapq.heappush(heap, nxt)  
                    
            out = heapq.heappop(heap)
            if out not in ansset:    #avoid redandunt (output)
                ansset.add(out)
                anslist.append(out) 
        #print()
        #print(anslist)
        return anslist[n-1]