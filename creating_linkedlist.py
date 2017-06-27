class LinkedList:
    head = None  # head will always contain the first Node of LinkedList

    def LinkedList(self):
        self.head = None

    class Node:
            data = 0
            next_node = None

            #Adds node to the start of the LinkedList
    def pushFront(self,input_data):
        new_node = self.Node()
        new_node.data = input_data
        #if LinkedList is empty head is None, assign value to head too

        if (self.head == None):
            new_node.next_node = None
            self.head = new_node

        else:
            #The new node next will point to previous head
            new_node.next_node = self.head
            #New node will become the new head
            self.head = new_node

    #Adds node to the end of the LinkedList
    def pushBack(self,input_data):

        #if LinkedList is empty head is None, assign value to head too
        if (self.head == None):
            first_node = self.Node()
            first_node.data = input_data
            first_node.next_node = None
            self.head = first_node
        else:
            new_node = self.Node()
            new_node.data = input_data
            new_node.next_node = None
            node_itr = self.head
            while(node_itr.next_node != None):
                node_itr = node_itr.next_node

            node_itr.next_node = new_node


    #Print the complete LinkedList by traversing it
    def printLinkedList(self):
        print("\n")
        #If LinkedList is not empty
        if (self.head !=None):
            node_iter = self.head
            #While node->next is not equal to empty , runs upto the end node not including the end node
            while(node_iter.next_node != None):
                print(node_iter.data   , end ="->")
                node_iter = node_iter.next_node

            print(node_iter.data  ,end="")

        else:
            print("LinkedList is empty")

ll = LinkedList()
#
ll.pushBack(5)
ll.pushFront(2)
ll.pushBack(10)
ll.pushBack(15)
ll.pushFront(1)
ll.pushBack(20)

ll.printLinkedList()
