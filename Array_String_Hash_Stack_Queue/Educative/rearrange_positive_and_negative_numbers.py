'''
QUESTION -
-----------
Given a list, re-arrange its elements in such a way that the negative elements appear on the left and positive elements appear at the right.
Note -  Its not necessary for you to maintain the order of the input list. While zero is NOT positive or negative, we will treat zero as a positive integer for this challenge! So zero will go on the right.
Sample Input - [10,-1,20,4,5,-9,-6]
Output - [-1,-9,-6,10,20,4,5]

APPROACH 1 -
-----------
    1. Create an empty output list.
    2. Traverse through the list once:
        i. check whether the element is less than Zero:
            a. If yes, then append that element to the output list.
    3. Traverse through the list for second time:
        i. check whether the element is greater than or equal to Zero:
            a. If yes, then append that element to the output list.
    4. Return output list.

    TIME COMPLEXITY - O(N).
    SPACE COMPLEXITY - This will not use any extra space except the output list.

APPROACH 2 - (Rearranging in place)
------------------------------------
    1. Initialize a pointer for positive element to 0.
    2. Iterate through the list:
        i. If the element is less than zero:
            a. check whether the pointer location and the element index is same or different. If same then increment the pointer.
            b. If different, then swap those 2 numbers.
    3. Return the input list.

    TIME COMPLEXITY - O(N)
'''

class Solution:
    def rearrangeList(self, list):
        output_list = []

        for num in list:
            if num < 0:
                output_list.append(num)

        for num in list:
            if num >= 0:
                output_list.append(num)

        return output_list

    def rearrangeListInPlace(self, list):
        leftPositivePointer = 0 # Pointer to keep track of leftmost positive number.
        for i in range(len(list)):
            if list[i] < 0:
                if i != leftPositivePointer:
                    # list[i], list[leftPositivePointer] = list[leftPositivePointer], list[i]
                    list[leftPositivePointer], list[i] = list[i], list[leftPositivePointer] #Swappint both numbers.
                leftPositivePointer += 1
        return list


if __name__ == '__main__':
    s = Solution()
    print(s.rearrangeList([-1, 2, -3, -4, 5]))
    print(s.rearrangeList([300, -1, 3, 0]))
    print(s.rearrangeList([0, 0, 0, -2]))
    print(s.rearrangeListInPlace([-1, 2, -3, -4, 5]))
    print(s.rearrangeListInPlace([300, -1, 3, 0]))
    print(s.rearrangeListInPlace([0, 0, 0, -2]))
