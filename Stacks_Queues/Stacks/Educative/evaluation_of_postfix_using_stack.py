'''
QUESTION -
----------
The usual convention followed in mathematics is the infix expression. Ex: 6 + 3 * 8 - 4
In postfix expression, the operators appear after the two numbers involved in the expression. It follows the BODMAS rule. Ex: 6 3 8 * + 4 -

Explanation of Postfix expression -
    1. From the first block of digits 6 3 8, we pick the last two which are 3 and 8.
    2. Reading the operators from left to right, the first one is *. The expression now becomes 3 * 8
    3.The next number is 6 while the next operator is +, so we have 6 + 8 * 3.
    4. The value of this expression is followed by 4, which is right before -. Hence we have 6 + 8 * 3 - 4.

Sample input: "921*-8-4+"
Sample output: 3

APPROACH -
----------
    Edge Cases:
        1. Check whether the inputStack is empty.
        2. Check whether the expression is empty. Print appropriate error message.
        3. Check whether there are atleast 2 operands before the operator is encountered. Otherwise the expression is incorrect.

    1. Create a stack to store numbers of the expression.
    2. Iterate through the expression:
        - Push the numbers to the stack.
        - If the element encountered is an operator, then pop 2 elements from the stack and perform the operation using that operator.
        - Push the result back into the stack.
    3. When the iteration is completed, the last number in the stack is the output. Pop that number.

TIME COMPLEXITY -
-----------------
    O(N) as we iterate through the list.

SPACE COMPLEXITY -
------------------
    O(N) as we create a stack to store operands.
'''

class Solution:
    def __init__(self):
        self.inputStack = []

    def enqueueIntoInputStack(self,expression):
        if len(self.inputStack) == 0: # Edge Case 1
            if len(expression) == 0: # Edge Case 2
                print("No expression found!")
                exit()
            for element in expression:
                if element.isdigit(): # If the element is digit, then push it to the stack.
                    self.inputStack.append(element)
                else:
                    if len(self.inputStack) >= 2: # Edge Case 3
                        num1 = self.inputStack.pop()
                        num2 = self.inputStack.pop()
                        evaluation = str(eval(num2 + element + num1)) # Performing operation of 2 popped elements.
                        self.inputStack.append(evaluation) # Pushing the result back to the stack.
                    else:
                        print("Postfix expression is incorrect")
                        exit()

        return self.inputStack.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.enqueueIntoInputStack("1*-8-4+")) # Output: "Postfix expression is incorrect"
    print(s.enqueueIntoInputStack("231*+9-")) # Output: -4
    print(s.enqueueIntoInputStack("")) # Output: "No expression found"
