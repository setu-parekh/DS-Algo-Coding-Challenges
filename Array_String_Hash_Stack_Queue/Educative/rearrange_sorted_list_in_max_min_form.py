'''
QUESTION -
----------
For a given sorted list, arrange elements in such a way that the maximum element appears at first position, then minimum at second, then second maximum at third and second minimum at fourth and so on.
Sample Input - [1,2,3,4,5]
Output - [5,1,4,2,3]

APPROACH 1 -
------------
    1. Create an empty output list.
    2. Initialize max and min pointers.
        - Max pointer points to the last element of the list.
        - Min pointer points to the first element of the list.
    3. Iterate through the list until max_pointer and min_pointer are at different index locations.
        - Append the element at max pointer and then decrement the pointer.
        - Append the element at min pointer and then increment the pointer.
    4. If max and min pointers are pointing towards same element:
        - then append that element to the list.
    5. Return output list

    TIME COMPLEXITY - O(N)

APPROACH 2 -
------------
    1. Create an empty list.
    2. Find the half length of the list as we will perform only half traversal instead of full.
    3. Iterate till the half length:
        - Starting from last, append each element to the output list. last_element_to_be_appended = list[-(i+1)]
        - Next append elements from starting.
        - Do this alternatively.
    4. Check whether the length of the list is even or odd.
        - If the list is odd, there will be a middle element which will be appended after the iteration gets over.
        - If the list is even, return the output list.

    TIME COMPLEXITY - O(N)
'''

class Solution:
    def rearrangeMaxMinListFullTraversal(self, list):
        length = len(list)
        output_list = []
        max_pointer = length - 1
        min_pointer = 0
        i = 0

        while max_pointer != min_pointer and i < length :
            if list[max_pointer] not in output_list:
                output_list.append(list[max_pointer])
                max_pointer -= 1
            if list[min_pointer] not in output_list:
                output_list.append(list[min_pointer])
                min_pointer += 1
            i += 1

        if max_pointer == min_pointer:
            output_list.append(list[max_pointer])

        return output_list

    def rearrangeMaxMinListHalfTraversal(self, list):
        length = len(list)
        half_length = length//2 # '//' operator divides 2 numbers and takes the floor value as answer. Eg - 9//2 = 4 instead of 4.5
        output_list = []

        for i in range(half_length):
            output_list.append(list[-(i+1)]) # Appending element from end
            output_list.append(list[i]) # Appending element from start

        if length%2: # If length of the list is odd.
            output_list.append(list[half_length])

        return output_list


if __name__ == '__main__':
    s = Solution()
    print(s.rearrangeMaxMinListFullTraversal([1,2,3,4,5]))
    print(s.rearrangeMaxMinListFullTraversal([1,2,3,4,5,6]))
    print(s.rearrangeMaxMinListHalfTraversal([1,2,3,4,5]))
    print(s.rearrangeMaxMinListHalfTraversal([1,2,3,4,5,6]))
