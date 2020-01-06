'''
QUESTION -
----------
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
    Input: "()"
    Output: true
Example 2:
    Input: "()[]{}"
    Output: true
Example 3:
    Input: "(]"
    Output: false
Example 4:
    Input: "([)]"
    Output: false
Example 5:
    Input: "{[]}"
    Output: true

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
    def isValid(self, s: str) -> bool:
        tempStack = []
        if len(s) == 0:
            return True

        for char in s:
            if char == '(' or char == '[' or char == '{':
                tempStack.append(char)
                continue
            else:
                if not tempStack:
                    return False
                stackTop = tempStack.pop()
                if stackTop == '(' and char != ')':
                    return False
                if stackTop == '[' and char != ']':
                    return False
                if stackTop == '{' and char != '}':
                    return False

        if not tempStack:
            return True
        else:
            return False

    def isValidUsingHashing(self, s: str) -> bool:
        tempStack = []
        paranthesisDict = {'{':'}', '(':')', '[':']'}

        for char in s:
            if char in paranthesisDict.keys():
                tempStack.append(char)
                continue
            else:
                if not tempStack:
                    return False
                stackTop = tempStack.pop()
                if char != paranthesisDict.get(stackTop):
                    return False
        if not tempStack:
            return True
        else:
            return False
