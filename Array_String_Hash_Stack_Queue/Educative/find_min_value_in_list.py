'''
QUESTION -
Given a list of size ‘n,’ find the minimum value in the list.
Sample Input - [9,2,3,6]
Output - 2

APPROACH -
    1. Initialize the min number to None.
    2. Iterate through the entire list and compare each element with the min value.
        i. If the element is smaller than the min value, update the min value.
    3. Return min value

    TIME COMPLEXITY - O(N)

'''

class Solution:
    def findMinValue(self, list):
        if not list:
            return None

        min_value = None

        for element in list:
            if min_value is None or min_value > element:
                min_value = element

        return min_value


if __name__ == '__main__':
    s = Solution()
    print(s.findMinValue([1,-4,0,10]))
