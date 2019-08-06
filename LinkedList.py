
from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None # helps to improve insert performance

    def traverse(self):
        node=self.head
        while node != None:
            print(node.val, end=" ")
            node = node.next
        print()

    def insert(self, node):
         if (self.head == None):
             self.head=node
             self.last=node
         else:
             self.last.next=node
             self.last=node

    def count(self):
        count=0
        node=self.head
        while node != None:
            count += 1
            node = node.next
        return count

    def delete(self, val, deleteAll=True): # default to delete all matching values
        node=self.head
        if node == None:
            return

        prevNode=None
        itIsHead=True
        while node != None:
            if (val == node.val):
                print("removed node val="+str(val))
                if (itIsHead == True): ### del as head
                    self.head = node.next
                else:
                    prevNode.next=node.next

                if (deleteAll == False):
                  return
            else:
                itIsHead=False

            prevNode=node
            node=node.next

        self.last=prevNode

######################################################################
# Test all scenarios
# 1) delete head
# 2) delete in the middle
# 3) delete tail
# 4) delete multiple occurrences

ll=LinkedList()

ll.insert(Node(1))
ll.insert(Node(1))
ll.insert(Node(2))
ll.insert(Node(1))
ll.insert(Node(3))
ll.traverse()

#ll.delete(2)
ll.delete(1, False)
#ll.delete(1)
#ll.delete(1, True)
#ll.delete(3)

### output ###
#1 1 2 1 3
#removed node val=3
#1 1 2 1

ll.traverse()

