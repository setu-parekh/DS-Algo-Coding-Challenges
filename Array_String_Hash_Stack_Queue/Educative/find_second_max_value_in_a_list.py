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

APPROACH 2 - Without Sorting
-----------------------------
    1. Initialize max_num and second_max_num to lowest number possible.
    2. Iterate through the list to find the maximum number.
    3. Iterate through the list 2nd time:
        i. check whether the number is not equal to the max number.
        ii. If not, then compare with the initialized second_max_number and update the value with each iteration.
    4. Return second_max_number.

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

    def secondMaxWithoutSorting(self, list):
        length = len(list)
        if not list or length == 1: # Testing edge cases.
            return None
        max_num = float('-inf')
        second_max_num = float('-inf')
        for num in list:
            if num > max_num:
                max_num = num
        for i in range(length):
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


if __name__ == '__main__':
    s = Solution()
    print(s.secondMaxValueWithSorting([9,9,-2,0,6]))
    print(s.secondMaxWithoutSorting([1,-2,0,6,10,10]))
    print(s.secondMaxWithoutSorting([1]))
