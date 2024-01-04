class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    q = collections.deque()
    if root:
        q.append(root)
    ans = []
    while q:
        temp = []
        for i in range(len(q)):
            curr = q.popleft()
            temp.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        ans.append(temp)
    return ans
