class Node:
    def __init__(self,v,s):
        self.valeur=v
        self.suivant=s

class PileBis:
  """structure de pile via liste chaînée"""
  def __init__(self):
      self.memory = None
    
  def push(self, item):
      self.memory = Node(item, self.memory)
    
  def pop(self):
      self.memory = self.memory.suivant

  def peek(self):
    return self.memory.valeur
  
  def is_empty(self):
    return self.memory == None


  def height(self):

    size = 0
    current = self.memory
    while current is not None:
      size += 1
      current = current.suivant

    return size

  def show(self):

    print("Pile: ")

    current = self.memory
    while current is not None:
      print(current.valeur)
      current = current.suivant

      

  



    
  

def creer_pile_vide_bis():
  return PileBis()