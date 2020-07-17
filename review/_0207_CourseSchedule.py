class Solution:
    
    #BFS (Topological Sort) [13%]
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_to_degree = self.getIndegree(numCourses, prerequisites)
        print("node_to_degree:", node_to_degree)
        
        start_nodes = [node for node in node_to_degree if node_to_degree[node]==0] #nodes with indegree=0 
        queue = collections.deque(start_nodes) 
        used = set()
        
        order = []   #answer
        while queue:
            node = queue.popleft()
            print("queue:", queue)
            print("node:", node)
            
            order.append(node)  #zero_degree node
            used.add(node)
            for p in prerequisites:  #can we not loop all the array?? 
                if p[1] == node:
                    node_to_degree[p[0]] -= 1  #neighbors' degree minus by 1
                    
                    #if neighbor became zero degree, add to queue
                    if node_to_degree[p[0]] == 0 and p[0] not in used: 
                        queue.append(p[0])
        print("order:", order)
        
        if len(order) == len(node_to_degree):
            return True
        return False
            
    # p[1] -> p[0]
    def getIndegree(self, numCourses, prerequisites):
        node_to_degree = {i:0 for i in range(numCourses)}
        for p in prerequisites:
            node_to_degree[p[0]] += 1 
        return node_to_degree