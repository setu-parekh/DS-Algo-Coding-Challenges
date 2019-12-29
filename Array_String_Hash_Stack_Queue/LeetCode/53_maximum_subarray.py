'''
QUESTION -
----------
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

APPROACH -
----------
Using Kadane's Algorithm:

    1. We will iterate over all the elements of the given list and find the max_continuous_sum and max_sum_so_far.
    2. At starting, the values of max_continuous_sum and max_sum_so_far will be same as the value of index = 0.
    3. If max_continuous_sum + input[i] < input[i], this means that the previous max was negative and we reset the max_continuous_sum = input[i]. Now we will look for new continuous array.
    4. If max_continuous_sum + input[i] > input[i], then we update the value of max_continuous_sum = max_continuous_sum + input[i].
    5. Then we check whether the max_continuous_sum > max_sum_so_far, if yes then max_sum_so_far = max_continuous_sum.

    Time Complexity -
    -----------------
    - As we iterated through the given list, time complexity is O(N)

    Space Complexity -
    ------------------
    O(1)

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_continuous_sum = nums[0]
        max_so_far = nums[0]

        for i in range(1,len(nums)):
            if max_continuous_sum + nums[i] < nums[i]:
                max_continuous_sum = nums[i]
            else:
                max_continuous_sum = max_continuous_sum + nums[i]
            if max_continuous_sum > max_so_far:
                max_so_far = max_continuous_sum

        return max_so_far
