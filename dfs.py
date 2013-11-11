from sys import argv
class Node:

	def __init__(self, item, left=None, right=None):
        	"""(Node, object, Node, Node) -> NoneType
        	Initialize this node to store item and have children left and right.
        	"""
        	self.item = item
        	self.left = left
        	self.right = right

	def dfs(self,value):
        if self.item == value:
            return true
        else:
    	   if self.left:
             self.left.dfs(value)
            if self.right:
                self.right(value)
            return false

#if __name__ == "__main__":
	#name,arg1,arg2=argv
	#b=Node(100)
	#b.depth()

x=Node(100,Node(1,Node(25),Node(34)),Node(6))
print x.search(6)
