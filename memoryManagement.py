'''
Two Handed Clock Memory Management System
Dylan Murray - 121747725
'''
class clock:

      def __init__(self):
            self.tail = None
            self.resetlist = []
      
      def addNode(self, process):
            # If the list is empty the initialise list.
            if self.tail == None:
                  return self.addWhenEmpty(process)
            # Else, Assign new node to beginning of the list as most recent item.
            temp = Node(process)
            # Add node to reset list.
            self.resetlist.append(temp)
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
      
      def print(self): 
            # print the list
            if (self.tail == None): 
                  print("List is empty") 
                  return
            temp = self.tail.next
            while temp: 
                  print(temp.process, end=" ") 
                  temp = temp.next
                  if temp == self.tail.next: 
                        break
      
      def getCount(self):
            # get the length of the list
            temp = self.tail.next
            count = 0     

            while(temp):
                count += 1
                temp = temp.next
            return count 
      

      def track(self):
            # set hands to starting positions
            bighand = self.tail.next
            length = self.getCount()
            temp = self.tail.next
            i = 0
            for i in range(1, length/2):
                temp = temp.next
            smallhand = temp

            # Check nodes and move hands
            while i < self.getCount()*2:
                  #split address and get the first two bits for smallhand
                  addr = id(smallhand)
                  binAddr = bin(addr)
                  bits = binAddr[2:4]
                  # check accessed and modified and advance hand
                  if bits != "11":
                        self.resetlist.append(smallhand)
                  smallhand = smallhand.next
                  # big hand checking if the oldest point of the reset 
                  # list is equal to the node its checking.
                  if bighand == self.resetlist[0]:
                        # swap with new process
                        return
                  bighand = bighand.next


class Node:
      
      def __init__(self, process):
            self.process = process
            self.next = None
