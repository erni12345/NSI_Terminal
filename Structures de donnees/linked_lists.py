class Node:
    def __init__(self, dataVal = None):
        self.dataval = dataVal
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None


    def print_list(self):
        print_val = self.headval
        while print_val is not None:
            print(print_val.dataval)
            print_val = print_val.nextval

    def longueurListe(self):
        size = 0
        val = self.headval
        while val != None:
            size += 1
            val = val.nextval

        return size

    def renvoieList(self):
        listVal = []
        val = self.headval
        while val != None:
            listVal.append(val.dataval)
            val = val.nextval

        return listVal


    def ajouter_debut(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode




list1 = LinkedList()
list1.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thursday")


list1.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4

print(list1.longueurListe())

