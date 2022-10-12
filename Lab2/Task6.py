class Node:
    def __init__(self, code:int, price:int|float):
        self.code = code
        self.price = price
        self.left_node = None
        self.right_node = None

    
class BinarySearchTree:            
    def __init__(self):
        self.root_node = None
    
    def add_child(self, code:int, price:int|float):
        if self.root_node is None:
            self.root_node = Node(code, price)
            return True
        
        return self.__add_child_helper(code, price, self.root_node)
        
    def __add_child_helper(self, code:int, price:int|float, root:Node):
        if root.code == code:
            return False
        elif code < root.code:                                             
            if root.left_node is None:
               root.left_node = Node(code, price)
               return True
            else:
                return self.__add_child_helper(code, price, root.left_node)
        else:
            if root.right_node is None:
                root.right_node = Node(code, price)
                return True
            else:
                return self.__add_child_helper(code, price, root.right_node)
      
    def contains(self, code:int):
        if self.root_node.code == None:
            raise Exception("Tree is empty!")
        elif self.root_node.code == code:
            return True
        else:
            return self.__contains_helper(self.root_node, code)

    def __contains_helper(self, root:Node, code:int):
        if code < root.code:
            if root.left_node is None:
                return False
            elif root.left_node.code == code:
                return True
            else:
                return self.__contains_helper(root.left_node, code)
            
        elif code > root.code:
            if root.right_node is None:
                return False
            elif root.right_node.code == code:
                return True
            else:
                return self.__contains_helper(root.right_node, code)
        else:
            return False  
        
    def in_order_traversal(self):
        if self.root_node is None:
            raise Exception("Tree is empty!")
        return self.__in_order_traversal_helper(self.root_node)
    
    def  __in_order_traversal_helper(self, node:Node):
        leaves = []
        
        if node.left_node is not None:
            leaves += self.__in_order_traversal_helper(node.left_node)
        
        leaves.append((node.code, node.price))
        
        if node.right_node is not None:
            leaves += self.__in_order_traversal_helper(node.right_node)
        
        return leaves
    
    def find_sum(self, code:int, quantity:int):
        if self.contains(code):
            return self.__find_sum_helper(self.root_node, code, quantity)
        else:
            raise Exception("Tree doesn't contain such product")

    def __find_sum_helper(self, root:Node, code:int, quantity:int):
        if code < root.code:
            return self.__find_sum_helper(root.left_node, code, quantity)
        elif  code > root.code:
            return self.__find_sum_helper(root.right_node, code, quantity)
        else:
            return root.price * quantity
        
if __name__ == "__main__":
    
    tree = BinarySearchTree()
    tree.add_child(1, 20)
    tree.add_child(9, 30)
    tree.add_child(4, 50)
    tree.add_child(3, 10)
    tree.add_child(8, 25)
    
    sum = tree.find_sum(4, 3)
    print(f"Sum: {sum}")
