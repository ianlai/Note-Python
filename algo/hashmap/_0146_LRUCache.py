# What data structures we need to use?
# Linear structure: array, linkedlist
# Update to new   : linkedlist 
# Get in O(1)     : hashmap 
# ==> So our LRU should use linkedlist + hashmap 

# What should we store in hashmap? 
# key  : key
# value: previous node (because we need to move the current to the tail) 
# ==> So we need to have dummy node 

class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next 
        
    def __str__(self):
        return "[" + str(self.key) + "," + str(self.value) + "]"
        
class LRUCache:
    is_debug = False
    
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.tail = None
        self.key_to_prev = {}
        self.dummy = LinkedNode()
    
    def push_tail(self, node):
        if self.tail is None:  #empty
            self.tail = node 
            self.dummy.next = node
            self.key_to_prev[node.key] = self.dummy
        else:
            self.tail.next = node
            self.key_to_prev[node.key] = self.tail
            self.tail = node

    def pop_head(self):
        new_head = self.dummy.next.next
        self.key_to_prev[new_head.key] = self.dummy  #update the map
        self.dummy.next = new_head                   #update the link  
        
    def kick_tail(self, node):
        #special case: only one node 
        if node == self.tail:
            return 
        #(1) remove node
        prev = self.key_to_prev[node.key]
        prev.next = node.next                   #update the link
        self.key_to_prev[node.next.key] = prev  #update the map
        
        #(2) attach node to tail
        self.push_tail(node)
        
    def get(self, key: int) -> int:
        #Search in map
        if key in self.key_to_prev:
            res = self.key_to_prev[key].next.value
            self.kick_tail(self.key_to_prev[key].next)
            self.debug("GET: (" + str(key) + ")")
            return res
        else:
            return -1 
        
    def put(self, key: int, value: int) -> None:
        #Search in map 
        if key in self.key_to_prev:  #update 
            node = self.key_to_prev[key].next
            node.value = value 
            self.kick_tail(node)
        else:                        #add 
            node = LinkedNode(key, value)
            self.push_tail(node)
            if len(self.key_to_prev) > self.capacity:
                head = self.dummy.next
                self.pop_head()
                del self.key_to_prev[head.key]
        self.debug("PUT: (" + str(key) + "," + str(value) + ")")
    
    def debug(self, msg):
        if not LRUCache.is_debug:
            return
        print(msg, end = " >> ")
        for e in self.key_to_prev:
            print(str(e) + ": " + str(self.key_to_prev[e]), end=" ")
        print()
        
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)