'''
QUESTION -
----------
https://leetcode.com/problems/happy-number/
Write an algorithm to determine if a number is "happy".

Note - A happy number is a number defined by the following process: Starting with any positive integer,            replace the number by the sum of the squares of its digits, and repeat the process until the number         equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those             numbers for which this process ends in 1 are happy numbers.
Example 1:
    Input: 19
    Output: True
    Explanation:
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1

Example 2:
    Input: 11
    Output: False
    Explanation:
        1² + 1² = 2
        2² = 4 -----------------> Cycle Starting
        4² = 16
        1² + 6² = 37
        3² + 7² = 58
        5² + 8² = 89
        8² + 9² = 145
        1² + 4² + 5² = 42
        4² + 2² = 20
        2² + 0² = 4 ------------> Cycle Found


APPROACH -
----------
Using Hash set:

    1. We will define a helper function to seperate the digits of the given number and return the sum of squares of each digit.
    2. We will keep on iterating till the value of sum is 1 and the num = sum has not been visited yet.
    3. If sum = 1, then it is a happy number.
    4. If we come across a number which was already in the visited list, that means there is a cycle and we will never reach to the value 1. Hence the number is not a happy number.

    Time Complexity -
    -----------------
    There are 2 parts of this Algo:
        1. sumOfSquares function
            - In order to find sum of squares of individual digits (K) of a given number (N), time taken depends upon number of digits in the number.
            - For example: N = 116, number of digits is 3. We will iterate 3 times to find the sum of squares of each digit.
            - This will take O(logN) time.
        2. Checking whether the number is in the visited list - O(1)
        2. How many times we called the above function:
            - We call the method, sumOfSquares until a cycle is encountered and the resulting sum is 1.
            - Number of times the method is called will depend upon the number of digits.
            - For example, a 3 digit number will never exceed 999. So the sum of digit squares will never cross 243. We will either come across a cycle or reach 1 till 243. This is a constant value.
            - Time complexity in this case is O(1)
    Overall time complexity is O(logN)

    Space Complexity -
    ------------------
    - visited set used O(N) space to store N numbers. N = number of times the iteration was done till N = 1 and no cycle found.

Using Two Pointers (Floyd's cycle finding algo):

    1. We will define a helper function to seperate the digits of the given number and return the sum of squares of each digit.
    2. We will initialze 2 pointers, slow and fast.
        - slow_pointer will move 1 step at a time.
        - fast_pointer will move 2 steps at a time.
    3. Next, we will keep on iterating and call the method until both pointers meet at a point (denoting a cycle) and fast_pointer = 1.
    4. If fast_pointer = 1, the given number is a happy number.
    5. If both pointers meet at some point, this indicates the presence of a cycle.

    Time Complexity -  Same as above.
    -----------------

    Space Complexity -
    ----------------
    - Since no extra space is used, space complexity is O(1)
'''
class Solution:
    def isHappyUsingHash(self, n: int) -> bool:
            def sumOfSquares(num):
                sumSquare = 0
                while num > 0:
                    num,mod = divmod(num,10)
                    sumSquare = sumSquare + mod**2

                return sumSquare

            visited = set()
            while n != 1 and n not in visited:
                visited.add(n)
                n = sumOfSquares(n)

            if n == 1:
                return True
            else:
                return False

    def isHappyTwoPointers(self, n: int) -> bool:
        def sumOfSquares(num):
                sumSquare = 0
                while num > 0:
                    num,mod = divmod(num,10)
                    sumSquare = sumSquare + mod**2

                return sumSquare

        slow_runner = n
        fast_runner = sumOfSquares(n)

        while fast_runner != slow_runner and fast_runner != 1:
            slow_runner = sumOfSquares(slow_runner)
            fast_runner = sumOfSquares(sumOfSquares(fast_runner))

        if fast_runner == 1:
            return True
        else:
            return False
