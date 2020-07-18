class Solution:
    
    # Example: 
    # 5
    # [[1,0],[2,1],[3,1],[4,3],[2,4]]
    
    # BFS - Topological Sort (store the graph, fast) [25%, 160ms] 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        print("Topological Sort 1 - store the graph")
        if numCourses == 0:
            return []

        nodeToDegree = self.scanIndegree(numCourses, prerequisites) 
        nodeToNodes  = self.scanNode(numCourses, prerequisites) 
        
        #print(nodeToDegree)
        #print(nodeToNodes)
        
        zeroNodes = []
        for i in range(len(nodeToDegree)):
            if nodeToDegree[i] == 0:
                zeroNodes.append(i)
        queue = collections.deque(zeroNodes)
        used = set()
        ans = []
        
        while queue:
            cur = queue.popleft()
            used.add(cur)
            ans.append(cur)
            for dst in nodeToNodes[cur]:
                if dst in used:
                    continue
                nodeToDegree[dst] -= 1
                if nodeToDegree[dst] == 0:
                    queue.append(dst)
        if len(ans) == numCourses:
            return ans
        return []
        
    def scanIndegree(self, numCourses, prerequisites) -> List[int]: #return list
        nodeToDegree = [0] * numCourses  #node -> indegree
        for e in prerequisites:
            nodeToDegree[e[0]] += 1
        return nodeToDegree
    
    def scanNode(self, numCourses, prerequisites): #return map 
        nodeToNodes = {}  #node -> node
        for i in range(numCourses):
            nodeToNodes[i] = []  
        for e in prerequisites:
            nodeToNodes[e[1]].append(e[0])
        return nodeToNodes
    
    #=================================================================================
    
    # BFS - Topological Sort (scan the edges, slow) [5%, 800ms]
    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        print("Topological Sort 2 - scan the edges")
        node_to_degree = self.getIndegree(numCourses, prerequisites)
        #print("node_to_degree:", node_to_degree)
        
        start_nodes = [node for node in node_to_degree if node_to_degree[node]==0]
        queue = collections.deque(start_nodes)
        used = set()
        #print("queue:", queue)
        order = []   #answer
        while queue:
            node = queue.popleft()
            order.append(node)  #zero_degree node
            used.add(node)
            for p in prerequisites:
                if p[1] == node:
                    node_to_degree[p[0]] -= 1  #neighbors' degree minus by 1
                    
                    #if neighbor became zero degree, add to queue
                    if node_to_degree[p[0]] == 0 and p[0] not in used: 
                        queue.append(p[0])
        #print("order:", order)
        
        if len(order) == len(node_to_degree):
            return order
        return []
            
    # p[1] -> p[0]
    def getIndegree(self, numCourses, prerequisites):
        #node_to_degree = {p[1]:0 for p in prerequisites}
        node_to_degree = {}
        for i in range(numCourses):
            node_to_degree[i] = 0 
        for p in prerequisites:
            node_to_degree[p[0]] += 1 
        return node_to_degree