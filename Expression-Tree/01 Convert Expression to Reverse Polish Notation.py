# Convert Expression to Reverse Polish Notation
# Given an expression string array, return the Reverse Polish notation
# of this expression. (remove the parentheses)
#
# Example
# For the expression [3 - 4 + 5] (which denote by ["3", "-", "4", "+", "5"]),
# return [3 4 - 5 +] (which denote by ["3", "4", "-", "5", "+"])
#

class Solution:
    # @param expression: A string list
    # @return: The Reverse Polish notation of this expression
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
