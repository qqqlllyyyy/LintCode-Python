# Expression Evaluation
# Given an expression string array, return the final result of this expression
#
# Example
# For the expression 2*6-(23+7)/(1+2), input is
# [
#   "2", "*", "6", "-", "(",
#   "23", "+", "7", ")", "/",
#   (", "1", "+", "2", ")"
# ],
# return 2
#
# Note
# The expression contains only integer, +, -, *, /, (, ).
#

# One step further based on the result of 'Convert Expression to Reverse Polish Notation':
# 'Evaluate Reverse Polish Notation' <-- This is a Leetcode problem.
class Solution:
    # @param expression: a list of strings;
    # @return: an integer
    def evaluateExpression(self, expression):
        # write your code here
        if len(expression) == 0: return 0
        calc_set = ['+', '-', '*', '/']
        RPN = self.convertToRPN(expression)
        if len(RPN) == 0: return 0 # If 'expression' is ['(','(','(',')',')',')'] 
        
        stack = []
        for i in range(len(RPN)):
            if RPN[i] not in calc_set:
                stack.append(int(RPN[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                if RPN[i] == '+':
                    stack.append(a + b)
                elif RPN[i] == '-':
                    stack.append(a - b)
                elif RPN[i] == '*':
                    stack.append(a * b)
                else:
                    stack.append(a / b) # Division is different from Leetcode!
        return stack.pop()
        
        
        
    
    
    
    def convertToRPN(self, expression):
        # write your code here
        n = len(expression)
        priority = [0 for i in range(n)]
        self.base = 0
        calc_set = ['+', '-', '*', '/']
        
        # Get a list of priority order
        for i in range(n):
            if expression[i] == '(':
                self.base += 10
            elif expression[i] == ')':
                self.base -= 10
            else:
                val = self.get(expression[i])
                priority[i] = val
        
        # Monotonous Stack        
        stack = []
        result = []
        for i in range(n):
            if expression[i] != '(' and expression[i] != ')':   
            # Skip parenthesis
            
                if len(stack) == 0:
                    stack.append(i)
                else:
                    # Check the prority of the last index in stack
                    if priority[i] > priority[stack[len(stack) - 1]]:
                        stack.append(i)
                    else:
                        while len(stack) > 0 and priority[i] <= priority[stack[len(stack) - 1]]:
                        # Note here is "<=", since if we have same level calculation
                        # like '+' and '-', the previous one shoud popped out.
                            temp = stack.pop()
                            result.append(expression[temp])
                        stack.append(i)
                            
        while len(stack) > 0:
            temp = stack.pop()
            result.append(expression[temp])
        return result
        
                    

    
    # Get Priority Order
    def get(self, a):
        if a == '+' or a == '-':
            return self.base + 1
        if a == '*' or a == '/':
            return self.base + 2
        return float("infinity")
