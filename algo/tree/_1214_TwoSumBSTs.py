# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if root1 is None:
            return False
        if root2 is None:
            return False
        arr1 = []
        arr2 = []
        self.convertToArr(root1, arr1)
        self.convertToArr(root2, arr2)
        p1, p2 = 0, len(arr2) - 1
        
        while p1 < len(arr1) and p2 >= 0:
            sum = arr1[p1] + arr2[p2]
            if sum == target: 
                return True
            elif sum < target:
                p1 += 1
            elif sum > target: 
                p2 -= 1 
        return False

        
    def convertToArr(self, node: TreeNode, arr:List):
        if node is None:
            return
        self.convertToArr(node.left, arr)
        arr.append(node.val)
        self.convertToArr(node.right, arr)
        return 
        