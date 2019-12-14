'''
QUESTION -
----------
Create Stack using class and write methods:
    1. To check whether the stack is empty.
    2. Push element into the stack.
    3. Pop element from the stack.
    4. Return the topmost element.
    5. Find the size of the stack.

'''
class Stack:
    def __init__(self):
        self.stackList = []

    def size(self):
        return len(self.stackList)

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.stackList[-1]

    def push(self,value):
        self.stackList.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stackList.pop()

if __name__ == '__main__':
    s = Stack() # Creating object for class mystack.
    for i in range(5):
        s.push(i) # Calling method push on object stack.
    print(s.stackList) # Output is in the form of list: [0,1,2,3,4]
    print("Topmost element in the stack is {}".format(s.top())) # Output: Topmost element is 4.
    print("Popped element: {}".format(s.pop())) # Output: 4
    print("Stack after popping topmost element: {}".format(s.stackList)) # Output: [0,1,2,3]
    print("Size of the stack after popping is: {}".format(s.size())) # Output: 4
