from sys import argv
class Node:

	def __init__(self, item, left=None, right=None):
        	"""(Node, object, Node, Node) -> NoneType
        	Initialize this node to store item and have children left and right.
        	"""
        	self.item = item
        	self.left = left
        	self.right = right

	def depth(self):
    		left_depth = self.left.depth() if self.left else 0
    		right_depth = self.right.depth() if self.right else 0
    		return max(left_depth, right_depth) + 1

#if __name__ == "__main__":
	#name,arg1,arg2=argv
	#b=Node(100)
	#b.depth()

x=Node(100,Node(1,Node(25),Node(34)),Node(6))
print x.depth()
