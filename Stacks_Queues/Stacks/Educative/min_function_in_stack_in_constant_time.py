'''
QUESTION -
----------
Write a program such that it has a getMin() function, which when called always returns the minimum element from the stack in O(1) time. The value is not popped from the stack. It is just returned.
Design a stack that supports: push, pop, top and retrieving minimum element in constant time.

InputStack = [9, 3, 1, 4, 2, 5]
minimum element = 1

APPROACH -
----------
    Edge Cases:
        1. check whether the input stack is empty. If yes, then return -1 when calling top() and getMin()
           function.

    1. Initialize 2 stacks: inputStack and minStack
    2. push():
        - Initially both lists will be empty so push the value into both stacks.
        - if stacks are not empty:
                - append value to inputStack
                - compare the value with minStack[-1].
                    - If value < minStack[-1], then push that value to minStack.
                    - Else, append minStack[-1] to minStack to synchronize the lengths of both stacks.
    3. pop():
        - pop top element from both the stacks.
        - return only from inputStack
    4. top():
        - check for the edge case. Return -1 if the inputStack is empty.
        - Return inputStack[-1]
    5. getMin():
        - check for the edge case. Return -1 if the inputStack is empty.
        - Return minStack[-1]

TIME COMPLEXITY -
-----------------
O(1). All the above operations are O(1)

SPACE COMPLEXITY -
------------------
O(N) as we created temporary minStack
'''

class Solution:
    def __init__(self):
        self.inputStack = []
        self.minStack = []

    def push(self, value):
        if len(self.inputStack) == 0:
            self.inputStack.append(value)
            self.minStack.append(value)
        else:
            self.inputStack.append(value)
            if value < self.minStack[-1]:
                self.minStack.append(value)
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self):
        if len(self.inputStack) != 0:
            self.minStack.pop()
            return self.inputStack.pop()

    def top(self):
        if len(self.inputStack) == 0: # Edge Case 1
            return -1
        else:
            return self.inputStack[-1]

    def getMin(self):
        if len(self.inputStack) == 0: # Edge Case 1
            return -1
        else:
            return self.minStack[-1]


if __name__ == '__main__':
    s = Solution()
    s.push(5)
    s.push(3)
    s.push(4)
    s.push(15)
    s.push(2)
    s.push(10)
    print(s.getMin()) # Output: 2
    s.pop() # Pops 10
    s.pop() # Pops 2
    print(s.getMin()) # Output: 3
    s.push(0) # inputStack = [5,3,4,15,0]
    print(s.getMin()) # Output: 0
    print(s.top()) # Output: 0
