
class Node:
    def __init__(self, data = None):
      self.left = None
      self.right = None
      self.data = data 

  
    def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data


    def order(self, data):
        if not (isinstance(data, int) or data < 0):
            raise ValueError('Invalid input')
        if data == self.data[0]:
            return self.data
        elif data < self.data[0]:
            return self.left.order(data) if self.left is not None else False
        elif data > self.data[0]:
            return self.right.order(data) if self.right is not None else False

    def get_cost(self, code, quantity):
        try:
            return quantity * self.order(code)[1]
        except TypeError:
            print('The product does not exist.')


    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print(self.data),
      if self.right:
         self.right.PrintTree()

def tree_size(tree):
    return 0 if tree is None else tree_size(tree.left) + 1 + tree_size(tree.right)


def get_products_cost(tree):
    total = 0
    max_size = tree_size(tree)
    size = int(input(f'Enter the number of products: {max_size} '))
    if not (isinstance(size, int)):
        raise ValueError
    for i in range(size):
        a = tuple(map(int, input('Code of a product: Quantity: (split numbers with space) ').split(' ')))
        total += tree.get_cost(a[0], a[1])
    return total  




tree = Node()
tree.insert((1, 665.6))
tree.insert((2, 45))
tree.insert((8, 10))
tree.insert((9, 78.999))
tree.insert((5, 67.90))
tree.insert((100, 1))
tree.PrintTree()
print("Final cost is:", get_products_cost(tree))