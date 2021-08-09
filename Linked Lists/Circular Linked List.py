#!/usr/bin/env python
# coding: utf-8

# # Circular Linked List

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


# In[ ]:


class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        """Print the entire linked list."""
        if self.head is None:
            print("Empty List!")
            return
        temp = self.head
        while True:
            print(self.data, end = " ")
            temp = temp.nextNode
            if (temp == self.head):
                break
    def length(self):
        """Find the length of a linked list."""
        length = 0
        if self.head is None:
            return length
        
        temp = self.head
        while True:
            length+=1
            temp = temp.nextNode
            if (temp == self.head):
                break
        return length
    
    def push(self, data):
        """Append data to end of a linked list."""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.nextNode = self.head
            return
        temp = self.head
        node.nextNode = self.head
        while (temp.nextNode != self.head):
            temp = temp.nextNode
        temp.nextNode = node
    
    def insert_at_loc(self, data, loc):
        """Insert data at a specific location in linked list. Indexing starts at 0."""
        node = Node(data)
        if self.head is None:
            print("Empty List!")
            return
        elif (self.length() - 1) < loc:
            print("Location out of bounds!")
            return
        else:
            temp = self.head
            count = 0
            while count < loc:
                temp = temp.nextNode
                count += 1
            node.nextNode = temp.nextNode
            temp.nextNode = node
    
    def insert_at_beginning(self, data):
        """Insert data at the beginning of a Linked List."""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.nextNode = self.head
            return
        temp = self.head
        node.nextNode = self.head
        while temp.nextNode != self.head:
            temp = temp.nextNode
        temp.nextNode = node
        self.head = node
        
    def pop(self):
        """Delete the last node from linked list."""
        if self.head is None:
            print("Empty List!")
            return
        temp = self.head
        while (temp.nextNode.nextNode != self.head):
            temp = temp.nextNode
        temp.nextNode = self.head
    
    def delete(self, data):
        """Delete node with given data."""
        if self.head is None:
            print("Empty List!")
            return
        elif self.head.data == data:
            temp = self.head
            while temp.nextNode != self.head:
                temp = temp.nextNode
            temp.nextNode = self.head.nextNode
            self.head = self.head.nextNode
        else:
            temp = self.head
            flag = False
            while temp.nextNode.data != data:
                temp = temp.nextNode
                if temp.nextNode == self.head:
                    print("Element not in list!")
                    flag = True
                    break
            if not(flag):
                temp.nextNode = temp.nextNode.nextNode
    
    def delete_at_loc(self, loc):
        """Delete data at a given location. Location starts from 0"""
        if self.head is None:
            print("Empty List")
            return
        
        elif (self.length() -1 )< loc:
            print("Location is out of bounds!")
            return
        
        else:
            temp = self.head
            count = 0
            while count<loc:
                temp = temp.nextNode
                count+=1
            temp.nextNode = temp.nextNode.nextNode
            
    def delete_list(self):
        """Delete the entire list itself."""
        #In Python, garbage collection happens, so just deleting the reference to the head will delete the list.
        self.head = None
    
    def search(self, data):
        """Search an element within the list."""
        count = 0
        if self.head is None:
            print("Empty List")
            return
        elif self.head.data == data:
            print("Element found at location {}: index {}".format(count+1, count))
            return

        temp = self.head
        flag = False
        while temp.nextNode != self.head:
            if temp.data == data:
                flag = True
                print("Element found at location {}: index {}".format(count+1, count))
            count += 1
        if not(flag):
            print("Element Not Found!")
            return
    
    def get_nth_node(self, n):
        if self.head is None:
            print("Empty List")
            return
        elif (self.length() - 1) < n:
            print("Out of bounds!")
            return
        else:
            temp = self.head
            count = 0
            while count < n:
                temp = temp.nextNode
                count+=1
            print(temp.nextNode.data)
            return temp.nextNode.data


# In[ ]:




