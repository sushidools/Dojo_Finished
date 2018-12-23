class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, *nums):
        for i in range(0, len(nums)):
            if type(nums[i]) is list or type(nums[i]) is tuple:
                for n in nums[i]:
                    self.result += n
            else:
                self.result += nums[i]
        return self
    def subtract(self, *nums):
        for i in range(0, len(nums)):
            if type(nums[i]) is list or type(nums[i]) is tuple:
                for n in nums[i]:
                    self.result -= n
            else:
                self.result -= nums[i]
        return self
    def finish(self):
        print(self.result)
x = MathDojo()
x.add(2).add(2,5,1).subtract(3,2).finish()
    

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = Node
    def printAllValues(self):
        runner = self.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)
    def addNode(self,value):
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        node = Node(value)
        runner.next = node