'''
QUESTION -
Given a list, find the first integer which is unique in the list. Unique means the number does not repeat and appears only once in the whole list.
Sample input - [9,2,3,2,6,6]
Output - 9

APPROACH -
    1. Create an empty dictionary.
    2. Iterate through the list:
        i. Add the integer to dictionary is not present already.
        ii. Increment the count of the integer if already present.
    3. Iterate through the keys in the dictionary.
        i. If the value corresponding to the key == 1, then return that key and this will break the loop.

    TIME COMPLEXITY - O(N). It will use extra space for the dictionary.

'''

class Solution:
    def findFirstUnique(self, list):
        count_dict = {}
        for num in list:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        for key in count_dict.keys():
            if count_dict[key] == 1:
                return key


if __name__ == '__main__':
    s = Solution()
    print(s.findFirstUnique([9,2,3,2,6,5,6,9]))
