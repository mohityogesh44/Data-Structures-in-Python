#!/usr/bin/env python
# coding: utf-8

# # Stack using Linked Lists

# Linked List node. It will store data for stack and also point to the next element in stack.
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


# In Stack, the linked list formed will be 1 <-2 <- 3 <- 4 <- .... instead of 1 -> 2 -> 3 -> 4 -> .....
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        # Create a Node with Data
        newNode = Node(data)
        # This new node will be pointing to old head
        newNode.nextNode = self.head
        # Make this new node as head
        self.head = newNode
        
    def pop(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.nextNode
        temp.next = None
        return temp.data
    
    def peek(self):
        if self.head is not None:
            return self.head.data
        return self.head
    
    def empty(self):
            return self.head == None
    
    def size(self):        
        length = 0
        if self.head is None:
            return length
        temp = self.head
        while temp:
            length +=1
            temp = temp.nextNode
        return length
    
    def show(self):
        #Reference of head in a temporary variable
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.nextNode
        
    # Fancy Overriding way of showing the whole Stack.
    # __str__ method gets called when print is used.
    #So we can override to print our instance using print().
    
    def __str__(self):
        temp = self.head
        out = ""
        while temp:
            out += str(temp.data)+" "
            temp = temp.nextNode
        return out.strip(" ")


if __name__=="__main__":
   
    s = Stack()

    print(s.empty())
    
    print(s.push(5))
    print(s.push(7))
    print(s.push(35))
    print(s.push(79))
    print(s.push(102))
    
    print(s)
    
    print(s.peek())
    print(s.empty())
    print(s.size())
    print(s.pop())
    print(s)
    s.show()