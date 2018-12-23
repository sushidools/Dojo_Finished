class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    def add_node(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
        return self
    def print_all_values(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))
    
    def remove_node(self, value):
        prev = None
        runner = self.head
        while(runner.next != None):
            if runner.value == value:
                if prev:
                    prev.next = runner.next
                else:
                    self.head = runner.next
            runner = runner.next
        return self
    
    def display(self):
        result = []
        runner = self.head
        while(runner):
            result.append(runner.value)
            runner = runner.next
        print(result)
        return self


list = SList(5)
list.add_node(7)
list.add_node(9)
list.add_node(1).display()
list.remove_node(9)
list.remove_node(5)
list.remove_node(1).display()

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        if self.head == None:
            self.head = node
        else:
            runner = self.head
            while(runner.next != None):
                runner = runner.next
            runner.next = node
        return self