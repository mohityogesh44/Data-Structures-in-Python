#!/usr/bin/env python
# coding: utf-8

# # Stack
# 
# Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be `LIFO(Last In First Out)` or `FILO(First In Last Out)`.
# 
# ### Operations associated with Stack:
#      1. push() : Insert an element on top.
#      2. pop() : Remove the element on top.
#      3. peek(): Return the topmost element from Stack.
#      4. empty(): Check if the Stack is empty.
#      5. size(): Return the size of Stack. 
#     *6. show(): Adding a show method to print all the elements in stack.



class Stack:
    
    def __init__(self):
        # Initialize an Empty List
        self.items = []
        
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
        
    # Fancy Overriding way of showing the whole Stack.
    # __str__ method gets called when print is used.
    #So we can override to print our instance using print().
    def __str__(self):
        return str(self.items)
    


if __name__=="__main__":

    stack = Stack()
    
    print(stack.size())
    print(stack.empty())

    print(stack.push(10))
    print(stack.push(20))
    print(stack.push(5))
    print(stack.push(2))
    print(stack.push(7))
    print(stack.push(9))
    
    print(stack.size())
    print(stack.empty())
    stack.show()
    print(stack)