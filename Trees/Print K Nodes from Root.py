class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

def KDistance(root,k):
    arr = []
    def helper(root,k):
        if not root:
            return
        if k==0:
            arr.append(root.data)
        else:
            helper(root.left,k-1)
            helper(root.right,k-1)
    helper(root,k)
    return arr
