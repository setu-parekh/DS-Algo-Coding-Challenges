'''
QUESTION -
----------
Write a program to find the next greater number for each element in the list. For each iteration, check for the elements in the list appearing after the current node.
The next greater element for the max element of the list and the last element is -1.
Sample Input: [4, 6, 3, 2, 8, 1]
Output: [6,8,8,8,-1,-1]

APPROACH -
----------
    Edge Case:
        1. Check whether the input list is empty. If empty, the return null.

    1. Initialize a result list = [-1] * length of input list.
    2. Find the max element from the list.
    3. Perform nested iterations:
        - Outer Loop: iterate through i=0 till 2nd last element of the list as next max for last element of   the list is -1 only.
        - Check whether input_list[i] = max element. If so then continue iterating through the outer loop     without doing anything.
        - Inner Loop: iterate through i+1 till end of the list comparing each element with input_list[i].     Replace the ith element of result list as input_list[j]. Break the loop when 1st max element        found.
    4. Return the result list.

TIME COMPLEXITY -
-----------------
O(N^2) because of nested loops.

SPACE COMPLEXITY -
------------------
O(1) as space occupied by input and result list are not considered as space complexity.
'''

class Solution:

    def nextMax(self,inputList):
        result = [-1]*len(inputList)
        if len(inputList) == 0:
            return []

        max_element = max(inputList)

        for i in range(0, len(inputList)-1):
            if inputList[i] == max_element:
                continue
            for j in range(i+1, len(inputList)):
                if inputList[j] > inputList[i]:
                    result[i] = inputList[j]
                    break

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.nextMax([4,6,3,8,2]))
    print(s.nextMax([10,9,5,3,0]))
    print(s.nextMax([0,0,0,5,0]))
    print(s.nextMax([0,0,0,0,0]))
