class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def postorder(root):
    if(root):
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")
        
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(8)
root.left.right=Node(7)
postorder(root)
    
