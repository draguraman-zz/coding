from sys import argv
class Node:

	def __init__(self, item, left=None, right=None):
        	"""(Node, object, Node, Node) -> NoneType
        	Initialize this node to store item and have children left and right.
        	"""
        	self.item = item
        	self.left = left
        	self.right = right


	def dfsWithPruning(self,value,map):
        map.add(hash(self)
        if self.item == value:
            return self
        else:

    	   if self.left and self.left not in map :
             val=self.left.dfs(value)
            
           if self.right and self.right not in map:
                self.right(value)
            return self


x=Node(100,Node(1,Node(25),Node(34)),Node(6))
 y =dfsWithPruning(4)


