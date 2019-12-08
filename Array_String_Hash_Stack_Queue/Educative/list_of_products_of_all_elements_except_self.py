'''
QUESTION -
Given a list, return a list where each index stores the product of all numbers in the list except the number at the index itself.
Input - A list of numbers (can even be floats, integers, and negative!)
Output - A list such that each index has a product of all the numbers in the list except the number stored at that index.

APPROACH 1 -
    1. Initialize 2 pointers:
        i. One for outer iteration.
        ii. Other for iteration through rest of the elements to calculate product.
    2. Initialize a product variable and an outlist list to store the products.
    3. Iterate both pointers till the length of the list.
        i. Iterate the product pointer while both the pointers are at different location.
        ii. Update the product
    4. Append the output list with the product.
    5. Reset the product variable to its initial value once 1 set of iteration is completed.
    6. Return output list.

    TIME COMPLEXITY - O(N^2)

APPROACH 2 -
    1. Initialize product variable.
    2. Create empty output list.
    3. Iterate through the list to calculate product of all elements of the list.
    4. Iterate through the list again:
        i. Divide overall product by each element.
        ii. Append the result to the output list.
    5. Return output list.

    * This approach will not work when the list consists of 0s.

    TIME COMPLEXITY - O(N)

APPROACH 3 -
    1. Initialize Left list L, right list R and output list with length = length of the given list.
    2. Prepare left list by iterating over elements of given list.
        i. L[i] = product of nums until i-1 as the index itself should not be considered.
    3. Prepare right list by iterating over elements of given list.
        i. R[i] = product of nums from i+1 till end of the nums in list.
    4. Iterate over L and R simultaneously. Multiply corresponding elements of L and R and store the products in output list.
        output_list[i] = L[i] * R[i]

    TIME COMPLEXITY - O(N) but this method uses extra space to store L, R and output list.

'''

'''
# Approach 1 -
class Solution:
    def findProduct1(self, list):
        i = 0 # Initializing pointer for outer iteration loop.
        j = 1 # Initializing pointer for product calculation.
        product = 1
        output_list = []
        while i < len(list) and j < len(list):
            while j != i:
                product = product * list[j]
                j = (j+1) % len(list)
            output_list.append(product)
            product = 1
            i += 1
            j = (i+1)%len(list)
        return output_list

if __name__ == '__main__':
    s = Solution()
    print(s.findProduct1([1,-2,3.1,4]))
'''
'''
# Approach 2 -
class Solution:
    def findProduct2(self, list):
        product = 1
        output_list = []
        for num in list: # Iterating to calculate overall product.
            product = product * num
        for num in list: # Iterating to divide the product by each element in the list.
            result = product/num
            output_list.append(result)
        return output_list

if __name__ == '__main__':
    s = Solution()
    print(s.findProduct2([1,2,3,4]))
'''
# Approach 3 -
class Solution:
    def findProduct3(self, list):
        if not list:
            return list

        list_length = len(list)
        # left = right = output_list = [1]*list_length is incorrect syntax in python. If written like this: left, right and output_list will refer to the same object instead of treating them as 3 different objects.
        left = [1] * list_length
        right = [1] * list_length
        output_list = [1] * list_length

        for i in range(1, list_length):
            left[i] = left[i-1] * list[i-1]

        for i in range(list_length-2, -1, -1):
            right[i] = right[i+1] * list[i+1]

        for i in range(list_length):
            output_list[i] = left[i] * right[i]

        return output_list


if __name__ == '__main__':
    s = Solution()
    print(s.findProduct3([1,2,3,4]))
