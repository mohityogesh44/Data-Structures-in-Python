#!/usr/bin/env python
# coding: utf-8

# ## Doubly Linked Lists

# In[1]:


class Node:
    def __init__(self, data):
        self.prevNode = None
        self.data = data
        self.nextNode = None


# In[1]:


class LinkedList:
    #Funtion to initialize an empty Linked List
    def __init__(self):
        self.head = None
    
    #Function to print a Linked List
    def display(self):
        """Print the entire linked list."""
        if self.head is None:
            print("Empty List")
            return
        #Reference of headin a temporary variable
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.nextNode
    
    def length(self):
        """Find the length of a linked list."""
        length = 0
        if self.head is None:
            return length
        temp = self.head
        while temp:
            length +=1
            temp = temp.nextNode
        return length
    
    #Functions to insert element
    def push(self, data):
        """Append data to end of a linked list."""
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp:
            temp = temp.nextNode
        temp.nextNode = node
        node.prevNode = temp
        
    def insert_at_loc(self, data, loc):
        """Insert data at a specific location in linked list. Indexing starts at 0."""
        node = Node(data)
        if self.head is None:
            print("List is empty")
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
            node.nextNode = temp.nextNode
            temp.nextNode.prevNode = node
            temp.nextNode = node
            node.prevNode = temp
            
    def insert_at_beginning(self, data):
        """Insert data at the beginning of a Linked List."""
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.nextNode = self.head
        self.head.prevNode = node
        self.head = node
    
    def pop(self):
        """Delete the last node from linked list"""
        if self.head is None:
            print("Empty List")
            return
        else:
            temp = self.head
            while temp.nextNode.nextNode:
                temp = temp.nextNode
            temp.nextNode = None
    
    def delete(self, data):
        """Delete node with given data."""
        if self.head is None:
            print("Empty List")
            return
        
        elif self.head.data == data:
            self.head = self.head.nextNode
            self.head.prevNode = None
            
        else:
            temp = self.head
            flag = False
            while temp.nextNode.data != data:
                temp = temp.nextNode
                if temp.nextNode is None:
                    print("Element not in list!")
                    flag = True
                    break
            if not(flag):
                temp.nextNode = temp.nextNode.nextNode
                temp.nextNode.prevNode = temp
            
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
            temp.nextNode.prevNode = temp
    
    def delete_list(self):
        """Delete the entire list itself."""
        #In Python, garbage collection happens, so just deleting the reference to the head will delete the list.
        self.head = None
    
    def search(self, data):
        """Search an element within the list."""
        if self.head is None:
            print("Empty List")
            return
        temp = self.head
        count = 0
        flag = False
        while temp:
            if temp.data == data:
                flag = True
                print("Element found at location {}: index {}".format(count+1, count))
            count += 1
        if not(flag):
            print("Element Not Found!")
            
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




