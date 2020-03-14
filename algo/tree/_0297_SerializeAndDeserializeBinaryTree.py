# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Skip the holes 
# [1,null,2,3,4] -> serialize to ['1', '#', '2', 3', '4'] 
class Codec:
    
    # tree -> string 
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            print("serialize: ", "")
            return ""
        
        queue = collections.deque([root])
        stringArr =[]
        string = ""
        layer = 1 
        num_in_layer = 2 ** (layer - 1)
        while queue:
            level = [] 
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)   #add even if it's None
                    queue.append(node.right)  #add even if it's None
                    stringArr.append(str(node.val))
                    #string += str(node.val) + ", "
                else:
                    stringArr.append("#")
                    #string += " # " + ", "
        #print("serialize: ", string)
        #return string 
        stringResult = ",".join(stringArr)
        print("serialize: ", stringResult)
        return stringResult
        
    # string -> tree 
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #strings = [s.strip() for s in data.split(",")] #remove the extra blanks
        #strings.pop() #remove the last empty string due to the last comma 
        
        strings = data.split(",")
        size = len(strings) 
        print("deserialize:", strings, " size:", size)
        if size <= 1:    #1 node will be 3 elements when doing the serialization 
            return None
        
        root = TreeNode(strings[0])
        queue = collections.deque([root])
        idx = 1
        while idx < size and queue:
            node = queue.popleft()
            if strings[idx] != "#":
                node.left = TreeNode(strings[idx])
                queue.append(node.left)
            else:
                node.left = None
            idx += 1
            if strings[idx] != "#":
                node.right = TreeNode(strings[idx])
                queue.append(node.right)
            else:
                node.right = None
            idx += 1  
        # self.createSubnodes(root, strings, 0, 0, size) 
        return root 

### Skip the holes 
### [1,null,2,3,4] -> serialize to ['1', '#', '2', 3', '4'] 
### We can't use a simple way to decide the leftIdx and rightIdx if we skip the holes 
#     def createSubnodes(self, node, strings, curIdx, num_of_skips, size):
#         
#         leftIdx = (curIdx + 1) * 2 - 1 - num_of_skips * 2
#         rightIdx = (curIdx + 1) * 2 - num_of_skips * 2
#         if not node:
#             return 
        
#         if leftIdx < size:
#             if strings[leftIdx] == "#":
#                 node.left = None
#             else:
#                 node.left = TreeNode(strings[leftIdx])
#                 self.createSubnodes(node.left, strings, leftIdx, size)  #don't know how to update the num_of_skips ...
#         if rightIdx < size:
#             if strings[rightIdx] == "#":
#                 node.right = None
#             else:
#                 node.right = TreeNode(strings[rightIdx])
#                 self.createSubnodes(node.right, strings, rightIdx, size)
        
#         return node
    
# Not skip the holes (TLE)
# [1,null,2,3,4] -> serialize to ['1', '#', '2', '#', '#', '3', '4'] (we should skip the two sharps between 2 and 3)    
class Codec_TLE:

    # tree -> string 
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        queue = collections.deque([root])
        string = ""
        layer = 1 
        num_in_layer = 2 ** (layer - 1)
        while queue:
            level = [] 
            #for _ in range(len(queue)):
            #print("num_in_layer:", num_in_layer)
            for _ in range(num_in_layer):
                node = queue.popleft()
                if node:
                    queue.append(node.left)   #add even if it's None
                    queue.append(node.right)  #add even if it's None
                    string += str(node.val) + ", "
                else:
                    queue.append(None)
                    queue.append(None)
                    string += " # " + ", "
            
            layer += 1
            num_in_layer = 2 ** (layer - 1)   
            
            #check 
            count = 0 
            #print("queue size:", len(queue))
            for x in queue:
                if x == None:
                    count += 1
            #print("count:", count)
            if count == num_in_layer:
                #print("END")
                break
            #print("layer: ", string)
            #print("--------------------")
                     

        print("serialize: ", string)
        return string 
            
        
    # string -> tree 
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        strings = [s.strip() for s in data.split(",")] #remove the extra blanks
        strings.pop() #remove the last empty string due to the last comma 
        
        print("deserialize:", strings)
        size = len(strings) 
        if size == 0:
            return None
        
        root = TreeNode(strings[0])
        self.createSubnodes(root, strings, 0, size) 
        return root 
    
    def createSubnodes(self, node, strings, curIdx, size):
        leftIdx = (curIdx + 1) * 2 - 1
        rightIdx = (curIdx + 1) * 2
        if not node:
            return 
        
        if leftIdx < size:
            if strings[leftIdx] == "#":
                node.left = None
            else:
                node.left = TreeNode(strings[leftIdx])
                self.createSubnodes(node.left, strings, leftIdx, size)
        if rightIdx < size:
            if strings[rightIdx] == "#":
                node.right = None
            else:
                node.right = TreeNode(strings[rightIdx])
                self.createSubnodes(node.right, strings, rightIdx, size)
        
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))