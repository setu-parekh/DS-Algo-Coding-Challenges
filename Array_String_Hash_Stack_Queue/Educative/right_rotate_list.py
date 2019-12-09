'''
QUESTION -
-----------
Given a list, rotate its elements by one index from right to left. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate by one element from the right though.
Sample Input -  A list and a number by which to rotate that list
                lst = [1,2,3,4,5]
                n = 3
Output - lst = [3,4,5,1,2]

APPROACH 1 - (By list methods)
-------------------------------
    1. Create an empty output list.
    2. Find the index of the element from where rotation is to be done as per given 'num'. It can be interpreted as last 'num' number of elements which should be shifted to extreme left.
    3. Populate the output list with right most elements.
    4. Extend the output list by adding original left most elements to the list.
    5. Return output_list.

    TIME COMPLEXITY - O(N)

APPROACH 2 - (By Slicing only)
-------------------------------
    1. First slicing the input list from end to last n elements.
    2. Next slicing the input list from start to last n elements.
    3. Combine both list into the output list.

    TIME COMPLEXITY - O(N)
'''

class Solution:
    def rightRotate(self, list, num):
        if num > len(list): # testing edge case.
            return False
        output_list = []
        rotate_start_index = len(list) - num
        output_list = list[rotate_start_index:] # Adding last n elements to the output list.
        output_list.extend(list[:rotate_start_index]) # Lastly appending initial len(list) - n elements to the output list.
        return output_list

    def rightRotateUsingSlicing(self, list, num):
        if num > len(list): # testing edge case.
            return False
        output_list = list[-num:] + list[:-num] # Slicing the input and then adding them into the output list.
        return output_list


if __name__ == '__main__':
    s = Solution()
    print(s.rightRotate([1,2,3,4,5,6,7], 3))
    print(s.rightRotateUsingSlicing([1,2,3,4,5,6,7], 3))
