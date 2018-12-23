class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
      
class SList:
    def __init__(self):
        self.head = None
        
    def add_node(self, value):
        node = Node(value)
      
        if self.head == None:
          self.head = node
        else:
          curr = self.head
          while curr.next != None:
              curr = curr.next
          curr.next = node
          
        return self

    def print_all_values(self):
          result = []
          if self.head == None:
              print(result)
          else:
              curr = self.head
              result.append(curr.val)
              while curr.next != None:
                  curr = curr.next
                  result.append(curr.val)
              print(result)
          
          return self
            
    def remove_node(self, value):
          if self.head == None:
            return None
          else:
              curr = self.head
              if curr.val == value:
                  self.head = curr.next
                  return curr
              if curr.next == None:
                return False
                
          while curr.next.next != None:
              if curr.next.val == value:
                  temp = curr.next
                  curr.next = curr.next.next
                  return temp
              curr = curr.next
                
          if curr.next.val == value:
                  temp = curr.next
                  curr.next = curr.next.next
                  return temp
          return False
      
slist = SList()
slist.print_all_values().add_node("A").print_all_values().add_node("B").print_all_values().add_node("C").print_all_values().remove_node("C")
slist.print_all_values()
