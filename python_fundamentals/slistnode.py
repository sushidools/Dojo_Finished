class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def printAllValues(self):
        result = []
        if self.head == None:
            print(result)
        else:
            runner = self.head
            result.append(runner.value)
            while(runner.next != None):
                runner = runner.next
                result.append(runner.value)
            print(result)
        return self
    def addNode(self,value):
        node = Node(value)
      
        if self.head == None:
            self.head = node
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = node
          
        return self
    def removeNode(self, value):
        if self.head == None:
            return self
        else:
            runner = self.head
            if runner.value == value:
                self.head = runner.next
                return self
            if runner.next == None:
                return self
            while runner.next.next != None:
                if runner.next.value == value:
                    temp = runner.next
                    runner.next = runner.next.next
                    return self
                runner = runner.next
            if runner.next.value == value:
                temp = runner.next
                runner.next = runner.next.next
                return self
            return self
    
x = SList()
x.printAllValues().addNode(5).addNode(7).addNode(9).addNode(1).printAllValues().removeNode(5).printAllValues()


