# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 재귀를 써서 지가 맞으면 왼쪽 오른쪽 -> bfs나 dfs로 순회
# 트리 순서가 자기, 왼쪽 자식, 오른쪽 자식 [1,1,2,1]
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Reached to the end of the tree: Both nodes are None
        if not p and not q:
            return True
        
        # One node is None
        if not p or not q:
            return False
        
        # Two values are different
        if p.val != q.val:
            return False

        # Compare its children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        