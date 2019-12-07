'''
QUESTION -
Implement a function which removes all the even elements from a given list.
Input - A list with random integers.
Output - A list with only odd integers

APPROACH 1 -
    1. Create an empty list to store odd integers.
    2. Iterate through the list and check whether the remainder is 0 or not when divided by 2.
    3. If the remainder is not 0, then append that number to the odd number list.

APPROACH 2 -
    1. Creating a new list for odd numbers using list comprehension python trick.

TIME COMPLEXITY -
    1. Best Case - O(1) when there is only 1 integer in the list.
    2. Average Case - O(N) as we will have to iterate through the list.
'''
# _____________________________________________________________________________________________________________
# Approach 1 -
'''
def removeEven1(list):
    odd_list = []
    for num in list:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

print("Odd numbers list is ",removeEven1([1,2,4,5,10,6,3])) # Output - [1,5,3]
print("Odd numbers list is ",removeEven1([2])) # Output - []
print("Odd numbers list is ",removeEven1([])) # Output - []
print("Odd numbers list is ",removeEven1([0])) # Output - []
'''
# _____________________________________________________________________________________________________________
# Approach 2 -
'''
# Defining a method to create a new list for storing odd integers. New list is created using list comprehension syntax.
def removeEven2(list):
    odd_list = [num for num in list if num % 2 != 0]
    return odd_list
print(removeEven2([1,2,4,5,10,6,3]))
'''
