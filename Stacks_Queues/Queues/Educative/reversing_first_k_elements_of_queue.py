'''
QUESTION -
----------
Write a function to reverse first K elements in a given queue. Input is a queue and a number K. We have to reverse first k elements of the queue and remaining elements will stay as is.
Sample Input: Queue = [1,2,3,4,5,6,7,9,10], k = 5
Ouput: Queue = [5,4,3,2,1,6,7,8,9,10]

APPROACH -
----------
    Edge Cases:
        1. Check whether the queue is empty. Return -1 if empty.
        2. Check whether k <= len(queue). If not then return False.

    1. Create an empty stack to push first k elements from queue.
    2. Iterate through queue from i=0 to i<k:
        - push element to stack.
        - remove that element from queue (Dequeue)
    3. Iterate through the length of the stack till it is empty:
        - pop the element and append it to the queue.
    4. Once the stack is empty and all elements have been enqueued to the queue, iterate through the queue from    j = 0 to j = size - k:
        - append element to the queue and remove that element(Dequeue).

TIME COMPLEXITY -
-----------------
O(N) as we iterate through the queue for removing and appending elements.

SPACE COMPLEXITY -
------------------
O(N) as we create a temporary stack.
'''

class Solution:
    def __init__(self):
        self.tempStack = []

    def reverseK(self,queue,k):
        if len(queue) == 0: # Edge Case 1
            return []

        if k <= len(queue): # Edge Case 2
            # Dequeuing the input queue and pushing first k elements to the stack.
            # As we remove one element from the queue, rest all elements will move one step to the left. So for every iteration we will be removing and appending the element at index = 0
            for i in range(0,k):
                self.tempStack.append(queue[0])
                queue.remove(queue[0])
            # Popping top element from the stack and appending it to the queue. Repeating this until the stack is empty.
            while len(self.tempStack) != 0:
                queue.append(self.tempStack.pop())
            # Appending initial size-k elements to the queue and removing them from thr front.
            # As we remove one element from the queue, rest all elements will move one step to the left. So for every iteration we will be removing and appending the element at index = 0
            for j in range(0,len(queue)-k):
                queue.append(queue[0])
                queue.remove(queue[0])

            return queue

        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.reverseK([1,2,3,4,5,6,7,9,10],5)) # Output: [5, 4, 3, 2, 1, 6, 7, 9, 10]
    print(s.reverseK([1,2,3,4,5],5)) # Output: [5, 4, 3, 2, 1]
    print(s.reverseK([1,2,3,4,5],6)) # Output: -1
    print(s.reverseK([],6)) # Output: []
