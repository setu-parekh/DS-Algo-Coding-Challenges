'''
QUESTION -
----------
Implement a function which will take a string containing only curly {}, square [], and round () parentheses. It will check whether the string containing parenthesis is balanced or not. Every opening parenthesis must have a closing one. The order in which they are arranged is important.

Sample Input: {[]} is balanced. Return True.
Sample Input: {[}] is not balanced. Return False.

APPROACH -
----------
    Edge Cases:
        1. Check whether the input string is empty or not.
        2. Check whether input string consists only {}, (), [] brackets.
        3. Check whether the temporary stack created during the execution is empty in the end after traversing through entire string.

    Method 1:
    1. Iterate through the string.
        - If char of the string is the opening parenthesis i.e, [ or ( or {:
                - append the char to the temp stack
                - continue for next chars until closing paranthesis is encountered.
        - Else:
                - pop the top element of the stack
                - if the top of stack and the next char in iteration are not opening-closing pairs:
                        return False
    2. Once the iteration is completed, if the stack is empty: return True

    Method 2 (Using Hashing):
    1. Create a dictionary with key:value = openingParenthesis:closingParenthesis
    2. Iterate through the expression:
        - If the char belongs to dic.keys():
                - append the char to the temp stack.
                - continue for next chars until closing paranthesis is encountered.
        - Else:
                - pop the top element of the stack.
                - if the char (not opening parenthesis) != corresponding value of top element(opening parenthesis which is the key in dict) in dict, then return False.
    3. Once the iteration is completed, if the stack is empty: return True


TIME COMPLEXITY -
-----------------
O(N) as we traversed through entire string once.

SPACE COMPLEXITY -
------------------
O(N) as temporary stack/dict was created.
'''

class Solution:
    def __init__(self):
        self.tempStack = []
    def checkBalance(self, inputExpression):
        if len(inputExpression) != 0: # Edge Case 1
            for char in inputExpression:
                if char == '(' or char == '[' or char == '{':
                    self.tempStack.append(char)
                    continue
                else:
                    if not self.tempStack: # Edge Case 2
                        return False

                    stackTop = self.tempStack.pop()

                    if stackTop == '[' and char != ']':
                        return False
                    if stackTop == '(' and char != ')':
                        return False
                    if stackTop == '{' and char != '}':
                        return False
            if not self.tempStack: # Edge Case 3
                return True
            else:
                return False
        else:
            return False

    def checkBalanceUsingHashing(self, inputExpression):
        paranthesisDict = {'{':'}', '(':')', '[':']'}

        if len(inputExpression) != 0: # Edge Case 1
            for char in inputExpression:
                if char in paranthesisDict.keys():
                    self.tempStack.append(char)
                    continue
                else:
                    if not self.tempStack: # Edge Case 2
                        return False
                    stackTop = self.tempStack.pop()
                    if char != paranthesisDict.get(stackTop):
                        return False
            if not self.tempStack: # Edge Case 3
                return True
            else:
                return False
        else:
            return False



if __name__ == '__main__':
    s = Solution()
    print(s.checkBalance("12")) #Output: False
    print(s.checkBalance("")) #Output: False
    print(s.checkBalance("[()]")) #Output: True
    print(s.checkBalance("{[({})]}")) #Output: True
    print(s.checkBalance("{[({)}]")) #Output: False

    print(s.checkBalanceUsingHashing("12")) #Output: False
    print(s.checkBalanceUsingHashing("")) #Output: False
    print(s.checkBalanceUsingHashing("[()]")) #Output: True
    print(s.checkBalanceUsingHashing("{[({})]}")) #Output: True
    print(s.checkBalanceUsingHashing("{[({)}]")) #Output: False
