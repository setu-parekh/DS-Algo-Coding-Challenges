'''
QUESTION -
----------
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Note: Assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Input = [2, 7, 11, 15], target = 9
Output = [2,7]

APPROACH -
----------
Brute Force:
    1. If the input list is empty: return []
    2. If no such 2 numbers found whose sum is equal to the target value, return []
    3. Initialize index pointer at i=0, j=i+1 and a complement_num variable.
    4. Iterate through the list and update the complement_num by doing target - i.
        - At each step, check whether the complement_num is present in the list.
        - If present, then return index of both nums

    Time Complexity -
    ------------------
    O(N^2) as we are performing nested iterations.

    Space Complexity -
    ------------------
    O(1) as no temporary list has been used.

Hashing:
    1. If the input list is empty:
            return []
    2. If the desired pair of numbers not found:
            return []
    3. Iterate through the input list:
        - Obtain the complementary number by doing: target - num
        - If the complementary num found in dict:
            return the indices of complimentary and the num
        - If complementary num not found in the dict:
            Add the current num to the dict.

    Time Complexity -
    -----------------
    O(N) as we iterated through the list. Finding key in dict using get() functions takes O(1) time.

    Space Complexity -
    ------------------
    Dictionary in the form {num:index} for storing N nums takes O(N) space.


'''

class Solution:
    def twoSumBruteForce(self, nums, target):
        complement_num = 0
        result = []
        L = len(nums)

        if L == 0:
            return []

        i = 0
        j = i+1

        while i < L: # Iterating through outer loop will take O(N) time
            while j < L: # Iterating through inner loop to compare each num with the complement_num will also take O(N) time.
                if nums[j] == target - nums[i]:
                    result.extend([i,j])
                    return result
                j += 1
            i += 1
            j = i+1

        return []

    def twoSumHashing(self, nums, target):
        visited = {}

        if not nums:
            return []

        for i in range(0, len(nums)):
            current_num = nums[i]
            complement_index = visited.get(target - current_num)
            if complement_index is not None and complement_index != i:
                return [complement_index, i]
            else:
                visited[current_num] = i
