'''
QUESTION -
----------
Write a program to implement a queue using two stacks. In other terms, get the enqueue and dequeue capabilities of Queue by using 2 stacks.

BASIC APPROACH -
----------------
Refer - https://medium.com/better-programming/how-to-implement-a-queue-using-two-stacks-80772242b88c
    1. Create two stacks.
    2. Adding elements to stack1.
    3. Remove the elements from stack1 and push them to stack2.
    4. This reverses the order and thus forms a queue.

APPROACH -
----------
    1. Initialize 2 stacks.
    2. Write an enqueue method to append elements into stack1.
    3. Check whether stack is empty before pushing elements of stack1 to stack2. Write appropriate error message if that happens.
    4. While stack1 is not empty, iterate to transfer elements from stack1 to stack2. This will reverse the order of elements in stack2.
    5. Pop elements from stack2. Popped element will be the first added element of stack1. Removing 1st element of the list is called Dequeue operation of Queue.

TIME COMPLEXITY: O(N)
---------------------
    These Pop and Push operations are performed on single element irrespective of size of the data set. We dont have to iterate through the list.
    - Appending elements into stackOne 1 at a time: Push O(1)
    - Popping topmost element from stackOne: Pop O(1)
    - Pushing that element into stackTwo: Push O(1)
    - Popping topmost element from stackTwo: Pop O(1)
    Runtime will increase as we add more elements.

SPACE COMPLEXITY: O(N)
----------------------
    - As we created two stacks for queue implementation, it utilizes space.
'''

class Solution:
    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    def enqueueIntoStackOne(self,value):
        self.stackOne.append(value) # Pushing elements into stack1. Recently added element is the top.

    def dequeuefromStackOne(self):
        if len(self.stackTwo) == 0:
            if len(self.stackOne) == 0:
                print("Stack is empty. Dequeue operation cannot be performed.")
                exit() # Exiting if we encounter this condition.
            # Popping topmost element from stack1 and pushing into stack2.
            while len(self.stackOne) > 0:
                topElement = self.stackOne.pop()
                self.stackTwo.append(topElement)

        return self.stackTwo.pop() # returning top of stack2 which is same as first element of stack1.


if __name__ == "__main__":
    s = Solution()
    s.enqueueIntoStackOne(2)
    s.enqueueIntoStackOne(10)
    s.enqueueIntoStackOne(24)
    print(s.stackOne) # Output: [2,10,24]
    print(s.dequeuefromStackOne()) # Output: 2
    print(s.dequeuefromStackOne()) # Output: 10
    print(s.dequeuefromStackOne()) # Output: 24
    s.enqueueIntoStackOne(20)
    print(s.stackOne) # Output: [20]
    print(s.dequeuefromStackOne()) # Output: 20
    print(s.dequeuefromStackOne()) #Output: "Stack is empty. Dequeue operation cannot be performed.""
