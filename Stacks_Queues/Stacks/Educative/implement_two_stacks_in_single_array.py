'''


https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/
'''

class Solution:
    def __init__(self,n):
        self.size = n
        self.list = [None] * n
        self.start = 0
        self.end = len(self.list)-1

    def pushStackOne(self,value1):
        # self.start = 0

        # Pushing elements to stack1 from start of the list.
        if self.start < self.end:
            self.list[self.start] = value1
            self.start = self.start+1
        else:
            print("Stack Overflow")
            exit(1)

    def pushStackTwo(self,value2):
        # self.end = len(self.list)-1
        # Pushing elements to stack2 from end of the list.
        if self.end >= self.start:
            self.list[self.end] = value2
            self.end = self.end-1
        else:
            print("Stack Overflow")
            exit(1)


    def popStackOne(self):
        # Poping topmost elements from Stack1.
        if self.start >= 0:
            top1 = self.list[self.start-1]
            self.start = self.start - 1
            return top1
        else:
            print("Stack Underflow")
            exit()

    def popStackTwo(self):
        # Poping topmost elements from Stack2.
        if self.end < len(self.list)-1:
            top2 = self.list[self.end+1]
            self.end = self.end + 1
            return top2
        else:
            print("Stack underflow")
            exit()


if __name__ == "__main__":
    s = Solution(6)
    s.pushStackOne(1)
    s.pushStackTwo(10)
    s.pushStackOne(2)
    s.pushStackTwo(9)
    s.pushStackOne(3)
    s.pushStackTwo(8)
    print(s.list) # Output: [1,2,3,8,9,10]
    print(s.popStackOne())
    print(s.popStackTwo())
    print(s.popStackOne())
    print(s.popStackTwo())
    print(s.popStackOne())
    print(s.popStackTwo())
    print(s.popStackOne())
    print(s.popStackTwo())
    # print(s.list)
