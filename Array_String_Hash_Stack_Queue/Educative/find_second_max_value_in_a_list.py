'''
QUESTION -
-----------
Given an array of size n, find the second maximum element in the list.
Sample Input - [9,2,3,6]
Output - 6

APPROACH 1 - With Sorting
--------------------------
    1. Find the length of the list.
    2. Sort the given list.
    3. If a list consist of max number occuring more than once, start iterating through the list from the end.
        i. if the value at current index is equal to the value at previous index:
            - decrement the index pointer.
        ii. if both values are different, then return list[i-1]

    TIME COMPLEXITY - O(NlogN)

APPROACH 2 - Without Sorting (Double Traversal)
------------------------------------------------
    1. Initialize max_num and second_max_num to lowest number possible.
    2. Iterate through the list to find the maximum number.
    3. Iterate through the list 2nd time:
        i. check whether the number is not equal to the max number.
        ii. If not, then compare with the initialized second_max_number and update the value with each iteration.
    4. Return second_max_number.

    TIME COMPLEXITY - O(N)

APPROACH 3 - Without Sorting (Single Traversal)
------------------------------------------------
    1. Initialize max_num and second_max_num to lowest number possible.
    2. Iterate through the list:
        i. if the element is greater than the max_num:
            - then update the max_num = element
            - update the second_max_num = max_num
        ii. if the element is smaller than the max_num:
            - check whether the element is greater than the second_max_num and not equal to the max_num.
                - If yes, then update the second_max_num.

    TIME COMPLEXITY - O(N)
'''
class Solution:
    def secondMaxValueWithSorting(self, list):
        length = len(list)
        if not list or length == 1: # These are edge cases.
            return None
        list.sort()
        # Iterating through the list to find the 2nd max value in case the max number is occuring more than once in the list.
        for i in range(length-1, -1, -1):
            if list[i] == list[i-1]:
                i = i-1
            else:
                return list[i-1]
        # return list[-2]

    def secondMaxDoubleTraversal(self, list):
        length = len(list)
        if not list or length == 1: # Testing edge cases.
            return None
        max_num = float('-inf')
        second_max_num = float('-inf')
        for num in list: # Iterating through the list to find the max number.
            if num > max_num:
                max_num = num
        for i in range(length): # Iterating through the list to find the second max number which is not equal to the max number.
            if list[i] == max_num:
                try:
                    i += 1
                except:
                    return second_max_num
            else:
                if list[i] > second_max_num:
                    second_max_num = list[i]
                    i += 1
        return second_max_num

    def secondMaxSingleTraversal(self, list):
        max_num = float('-inf')
        second_max_num = float('-inf')

        if not list or len(list) == 1: # Testing edge case.
            return None

        for i in range(len(list)):
            if list[i] > max_num:
                second_max_num = max_num
                max_num = list[i]
            elif (list[i] > second_max_num) and (list[i] != max_num):
                    second_max_num = list[i]

        return second_max_num


if __name__ == '__main__':
    s = Solution()
    print(s.secondMaxValueWithSorting([9,9,-2,0,6]))
    print(s.secondMaxDoubleTraversal([1,-2,0,6,10,10]))
    print(s.secondMaxDoubleTraversal([1]))
    print(s.secondMaxSingleTraversal([1,-2,0,6,10,10]))
    print(s.secondMaxSingleTraversal([1]))
