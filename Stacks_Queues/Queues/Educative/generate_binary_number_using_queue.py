'''
QUESTION -
----------
Write a program to generate binary numbers from 1 to any given number 'n'.
Sample Input: n = 3.
Output: convert 1,2,3 to binary. Result is ["1", "10", "11"]

APPROACH -
----------
    1. Initialise the result list to store the binary form of decimal numbers in string format.
    2. Define a function to convert decimal to binary.
        - Declare an empty list
        - For a given decimal number, divide it by 2 until num > 0:
            - append the remainder to the list.
            - divide by 2 again. Consider the floor value of the quotient
        - After appending all remainders to the list, reverse the list.
        - Return reversed list.
    3. Define a function to iterate from 1 to the given 'n'.
        - For each iteration, call function decimalToBinary() to convert each number to binary.
        - Append the binary to the result list in the form of string.
    4. Return the result list.

TIME COMPLEXITY -
-----------------
O(N) as we iterated through 1 till 'n'.

SPACE COMPLEXITY -
------------------
O(N) as we created temporary binary list to store the remainders.

'''
class Solution:
    def __init__(self):
        self.binList = []

    def decimalToBinary(self,num):
        binaryList = []
        while num > 0:
            r = num%2
            binaryList.append(r)
            num = num//2
        # Reversing list
        return ''.join(str(binaryList[i]) for i in range(len(binaryList)-1, -1, -1) )

    def findBin(self,n):
        for i in range(1,n+1):
            self.binList.append(self.decimalToBinary(i))

        return self.binList


if __name__ == '__main__':
    s = Solution()
    print(s.findBin(5))
