# Implement Queue by Two Stacks
# As the title described, you should only use two stacks to 
# implement a queue's actions.
# The queue should support push(element), pop() and top() where 
# pop is pop the first(a.k.a front) element in the queue.
# Both pop and top methods should return the value of first element.
#
# Example
# For push(1), pop(), push(2), push(3), top(), pop(),
# you should return 1, 2 and 2
#
# Challenge
# implement it by two stacks, do not use any other data structure
# and push, pop and top should be O(1) by AVERAGE.

"""
    In 'adjust', what if stack2 is not empty?
"""
class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        self.adjust()
        return self.stack2[len(self.stack2) - 1]

    def pop(self):
        # write your code here
        # pop and return the top element
        self.adjust()
        return self.stack2.pop()
        
        
        
    def adjust(self):
        if len(self.stack2) == 0:
            while  len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

