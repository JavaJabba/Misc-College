'''
Circular Linked List Memory Management System
'''
class CircularLinkedList:

      def __init__(self):
            self.tail = None
      
      def addNode(self, process):
            # If the list is empty the initialise list.
            if self.tail == None:
                  return self.addWhenEmpty(process)
            # Else, Assign new node to beginning of the list as most recent item.
            temp = Node(process)
            temp.next = self.tail.next
            self.tail.next = temp
            return self.tail

      def addWhenEmpty(self, process):
            # Initialise first item added to be the tail.
            temp = Node(process)
            self.tail = temp
            # Assign Links
            self.tail.next = self.tail
            return self.tail
      
      def traverse(self): 
        if (self.tail == None): 
            print("List is empty") 
            return
        temp = self.tail.next
        while temp: 
            print(temp.process, end=" ") 
            temp = temp.next
            if temp == self.tail.next: 
                break


class Node:
      
      def __init__(self, process):
            self.process = process
            self.next = None


if __name__ == '__main__': 
    llist = CircularLinkedList() 
    llist.traverse() 
    last = llist.addNode((222, 8000))
    llist.traverse() 