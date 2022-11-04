import math




def floor_log(x):
    return math.frexp(x)[1] - 1


class FibonnacciTree:
    def __init__(self, value, node):
        self.value = value
        self.node = node
        self.child = []
        self.order = 0
    
    def add_at_end(self, t):
        self.child.append(t)
        self.order += 1


class FibonacciHeap:
    def __init__(self):

        self.trees = []
        self.least = None
        self.count = 0

    def length(self):
        return len(self.trees)
        
    def insert_node(self, value, node):
        new_tree = FibonnacciTree(value, node)
        self.trees.append(new_tree)
        if self.least is None or self.least.value > value:
            self.least = new_tree
        self.count += 1
    
    def get_min(self):
        if self.least is None:
            return None
        return self.least.value
    
    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count -= 1
            return smallest.value, smallest.node


    def consolidate(self):
        aux = (floor_log(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order += 1

            aux[order] = x
        
        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.least is None or k.value < self.least.value:
                    self.least = k



