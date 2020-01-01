'''
QUESTION -
----------
Write a program which takes a stack and sorts all of its elements such that when they are popped and printed, they come out in ascending order.
Input - List of elements
Output - List of elements in descending order so that when popped from top, we obtain elements in ascending order.

APPROACH -
----------
    Edge Cases:
        1. Check whether the result list is empty before appending elements from the input list.
        2. Check whether the input list is having any elements or not. If the input list is empty, then print proper error message.
        3. If the length of input list is 1, then directly pop the element. Save the iteration through input list to find the max element.

    1. Initialize input and result stack.
    2. Create enqueue method to append elements to stack.
    3. Create a sorting method to arrange elements in descending order.
        - check all edge cases
        - iterate through stack list to find max element from input list using MAX() function.
        - Once the max element is obtained, append that to the result list and then remove that element from input list.
    4. Pop the element from top of result list and return.

TIME COMPLEXITY -
-----------------
    O(N) as we iterate through the list to find max element using max() function.

SPACE COMPLEXITY -
------------------
    O(N) where N = len(input_list) + len(result_list)

'''
class Solution:
    def __init__(self):
        self.inputStack = []
        # self.resultStack = []

    def enqueueIntoInputStack(self,value):
        self.inputStack.append(value) # Pushing elements into input stack. Recently added element is the top.

    def sortDescending(self):
        if len(self.resultStack) == 0: # Checking the condition if result list is empty before appending elements from input list.
            # Checking whether input list is empty. Printing appropriate error message.
            if len(self.inputStack) == 0:
                print("Empty input list")
                exit()
            # If there is only 1 element in input list, then pop that element directly.
            if len(self.inputStack) == 1:
                return self.inputStack.pop()
            # Iterating through the input list to find the max element and appending it to result list one by one.
            while len(self.inputStack) != 0:
                maxElement = max(self.inputStack)
                self.resultStack.append(maxElement)
                self.inputStack.remove(maxElement)

        return self.resultStack.pop()

    def sortDescendingInPlace(self):
        # Checking whether input list is empty. Printing appropriate error message.
        if len(self.inputStack) == 0:
            print("Empty input list")
            exit()
        # If there is only 1 element in input list, then pop that element directly.
        if len(self.inputStack) == 1:
            return self.inputStack.pop()
        # Iterating through the input list to find the max element and sorting in place
        i = 0
        j = 1
        max = float('-inf')
        while i < j and j < len(self.inputStack) :
            while j < len(self.inputStack):
                if self.inputStack[j] > max:
                    max = self.inputStack[j]
                j += 1
            if max > self.inputStack[i]:
                self.inputStack[i], max = max, self.inputStack[i] # Swapping
            print(self.inputStack)
            i += 1
            j += 1
        # return self.inputStack.pop()


if __name__ == "__main__":
    s = Solution()
    s.enqueueIntoInputStack(2)
    s.enqueueIntoInputStack(5)
    s.enqueueIntoInputStack(10)
    s.enqueueIntoInputStack(16)
    s.enqueueIntoInputStack(1)
    print(s.inputStack)
    print(s.sortDescendingInPlace())

    # print(s.sortDescending())
    # print(s.sortDescending())
    # print(s.sortDescending())
    # print(s.sortDescending())
    # print(s.sortDescending())
    # print(s.sortDescending())
