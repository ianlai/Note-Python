# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # General rules: 
    # store the coordinate (col, row) for each node, sort based on (col, row, value)
    
    
    # BFS Traverse: O(n) 
    # Global sorting (col, row, val): O(nlogn)
    # time complexity = [O(n*log(n)), 22%-44%] 
    
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        print("3")
        if not root:
            return []
        
        ans = []
        nodes = [(0, 0, root.val)]    #use list (for global sorting)
        
        # 1. Traverse (BFS)
        queue = deque([(0, 0, root)]) #col, row, node
        while queue:
            cur = queue.popleft()
            #print(cur[0], cur[1], cur[2].val)
            if cur[2].left:
                queue.append((cur[0]-1, cur[1]+1, cur[2].left))
                nodes.append((cur[0]-1, cur[1]+1, cur[2].left.val))
            if cur[2].right:
                queue.append((cur[0]+1, cur[1]+1, cur[2].right)) 
                nodes.append((cur[0]+1, cur[1]+1, cur[2].right.val)) 
        
        # 2. Global sort
        nodes.sort()
        
        # 3. Fill in the ans list with nodes list 
        ans.append([])
        ans[-1].append(nodes[0][2])     # add the first node (val)
        for i in range(1, len(nodes)):
            if nodes[i-1][0] != nodes[i][0]: #different col
                ans.append([])
            ans[-1].append(nodes[i][2]) # add the 2nd to last nodes (val)
        return ans
        
    # =============================================================
        
    # DFS Traverse, store the coordinate (col, row) for each node, sort based on (col, row, value)
    # One-level sorting: record min and max of col and col is continuous, so we sort (row, value) only 
    # Assume there are "k" (col), [O(k)* O(n/k * log(n/k)), 35%-68%] 
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        print("2")
        if not root:
            return []
        
        ans = []
        idxMinMax = [0, 0]   #0: min, 1:max
        idxToNodes = {}  #x -> [(row, value)]
        
        self.helper(root, 0, 0, idxToNodes, idxMinMax)
        #print(idxToNodes) 
        
        for col in range(idxMinMax[0], idxMinMax[1]+1, 1): #traverse from col-min to col-max
            ans.append([])
            
            nodesInCol = idxToNodes[col]
            for node in sorted(nodesInCol, key=lambda x:(x[0], x[1])): #sort based on row (row) then value 
                ans[-1].append(node[1])
                
        return ans
        
    def helper(self, root, col, row, idxToNodes, idxMinMax):
        if not root:
            return 
        
        # We can skip this if we declare idxToNodes defaultdict
        # i.e., idxToNodes = collections.defaultdict(list) 
        if col not in idxToNodes:
            idxToNodes[col] = []
        
        # Record min, max of col 
        if col < idxMinMax[0]: 
            idxMinMax[0] = col
        if col > idxMinMax[1]:
            idxMinMax[1] = col
            
        idxToNodes[col].append((row, root.val))
        
        self.helper(root.left,  col-1, row+1, idxToNodes, idxMinMax)
        self.helper(root.right, col+1, row+1, idxToNodes, idxMinMax)
        
    # =============================================================
    
    # DFS Traverse, store the coordinate (col, row) for each node, sort based on (col, row, value)
    # Two-level sorting: sort (col) then sort (row, value)
    # Assume there are "k" (col), [O(klog(k) * O(n/k * log(n/k)), 35%-68%] 
    def verticalTraversal1(self, root: TreeNode) -> List[List[int]]:
        print("1")
        if not root:
            return []
        
        ans = []
        idxToNodes = {}  #x -> [(row, value)]
        
        self.dfs(root, 0, 0, idxToNodes)
        #print(idxToNodes) 
        
        for nodesInCol in sorted(idxToNodes.items(), key=lambda x:x[0]):  #sort based on x (col)
            ans.append([])
            
            for node in sorted(nodesInCol[1], key=lambda x:(x[0], x[1])): #sort based on row (row) then value 
                ans[-1].append(node[1])
                
        return ans
        
    def dfs(self, root, col, row, idxToNodes):
        if not root:
            return 
        
        if col not in idxToNodes:
            idxToNodes[col] = []
            
        idxToNodes[col].append((row, root.val))
        
        self.dfs(root.left,  col-1, row+1, idxToNodes)
        self.dfs(root.right, col+1, row+1, idxToNodes)