class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return
        current=self.head
        while self.next:
            current=current.next
        current.next =newNode

