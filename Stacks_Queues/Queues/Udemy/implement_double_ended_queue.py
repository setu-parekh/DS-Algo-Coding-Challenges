'''
QUESTION -
----------
Write a program to implement a double ended queue. Define methods to enqueue elements to both front and end of the queue. Define a method to dequeue from front and end of the queue.

APPROACH -
----------
    1. Enqueue at front: Insert value at index 0.
    2. Enqueue at the end: Insert value at index -1.
    3. Dequeue from front: Remove element from index 0.
    4. Dequeue from end: Remove element from index -1.

TIME COMPLEXITY - O(1)
---------------

SPACE COMPLEXITY - O(1)
----------------
'''
class Solution:
    def __init__(self,list):
        self.queue = list

    def enqueueFront(self,value1):
        self.queue.insert(0,value1)

    def enqueueEnd(self, value2):
        self.queue.append(value2)

    def dequeueFromFront(self):
        if len(self.queue) == 0:
            return -1
        print("Length before dequeue: {}".format(len(self.queue)))
        self.queue.remove(self.queue[0])
        print("Length after dequeue: {}".format(len(self.queue)))

        return self.queue

    def dequeueFromEnd(self):
        if len(self.queue) == 0:
            return -1
        print("Length before dequeue: {}".format(len(self.queue)))
        self.queue.remove(self.queue[-1])
        print("Length after dequeue: {}".format(len(self.queue)))

        return self.queue


if __name__ == '__main__':
    s = Solution([4,7,9,3])
    s.enqueueFront(-1)
    print(s.queue)
    s.enqueueEnd(100)
    print(s.queue)
    print(s.dequeueFromFront())
    print(s.dequeueFromEnd())
