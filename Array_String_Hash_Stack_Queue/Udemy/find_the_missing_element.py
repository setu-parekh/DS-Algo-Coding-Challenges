'''
QUESTION -
https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20PRACTICE/Find%20the%20Missing%20Element%20.ipynb

APPROACH 1 - (This Approach gives error when the elements of the arrays are repeating)
    1. Compare the length of both arrays. As an element is missing in the 2nd array, the length wont match.
    2. If that is the case, iterate through the 1st array and check for the presence of each element of array1 in the array2. If a particular element is not present, then that is the missing element we are looking for.

APPROACH 2 -
    1. Adding all the numbers from 1st Array.
    2. Subtracting each number of 2nd Array from the summation of 1st Array.
    3. The remaining value will be the deleted number.

APPROACH 3 -
    1. Adding all the numbers from 1st Array.
    2. Adding all the numbers from 2nd Array.
    3. Subtracting both the summation values.
    4. The answer will be the deleted number.

APPROACH 4 -
    1. Sorting both arrays and then zipping it. Zipping both arrays together will club the similar position elements of each array into a tuple.
    2. Comparing both the elements of each tuple. If they dont match, then num1 of 1st array is missing.


COMPLEXITY -
    Approach 1 - O(N^2) as we need 2 loops. 1st for checking presence of each element of array1 in                     array2. 2nd for comparing the element of array1 with each element of array2 for presence              check.
    Approach 2 - O(N)
    Approach 3 - O(N)
    Approach 4 - Sorting of elements is O(log(N)). Since there is one iteration involved in the zipped                 array, overall complexity is O(Nlog(N))
'''
# _______________________________________________________________________________________________________
# Approach 1 -
# '''
def missingElementtheFinder1(array1, array2):
    # Comparing both lengths as 1 element is missing in array2.
    if len(array1) != len(array2):
        # Iterating through array1 to check the presence of each element of array1 in array2.
        for element in array1:
            # If a certain element not present, then it is our required element.
            if element not in array2:
                deleted_element = element
    print("{} is the missing number".format(deleted_element))

missingElementFinder1([1,2,3,4,5,6,7], [3,7,2,1,5,6])
missingElementFinder1([5,5,7,7], [5,7,7]) # This approach gives error with this example where values are repeating.
# '''
# _______________________________________________________________________________________________________
# Approach 2 -
# '''
def missingElementFinder2(array1, array2):
    sum = 0
    # Adding all the elements of array1.
    for element in array1:
        sum = sum + element
    # print(sum)
    # Subracting each element of array2 from the sum. The resulting value will be of the missing number in the array2.
    for element in array2:
        sum = sum - element
    print("{} is the missing number".format(sum))

missingElementFinder2([1,2,3,4,5,6,7], [3,7,2,1,5,6])
missingElementFinder2([5,5,7,7], [5,7,7])
# '''
# _______________________________________________________________________________________________________
# Approach 3 -
# '''
def missingElementFinder3(array1, array2):
    sum_array1 = 0
    sum_array2 = 0
    # Adding all elements of array1.
    for element in array1:
        sum_array1 = sum_array1 + element
    # Adding all elements of array2.
    for element in array2:
        sum_array2 = sum_array2 + element
    # Subtracting both summations will provide the deleted element from array2.
    deleted_element = sum_array1 - sum_array2
    print("{} is the missing number".format(deleted_element))

missingElementFinder3([1,2,3,4,5,6,7], [3,7,2,1,5,6])
missingElementFinder3([5,5,7,7], [5,7,7])
# '''
# _______________________________________________________________________________________________________
# Approach 4 -
def missingElementFinder4(array1, array2):
    # Sorting both arrays so that missing number can be easily found.
    array1.sort()
    array2.sort()
    # zip function clubs both arrays putting the similar position elements of each array into a tuple. eg - ([1,2,3,4,5,6,7], [3,7,2,1,5,6]) is zipped as [(1,3), (2,7), (3,2)...].
    # Since both arrays were sorted, the num1 and num2 in the tuples will match unless the number is missing.
    for num_1, num_2 in zip(array1, array2):
        if num_1 != num_2:
            return num_1
    # If num1 and num2 matches in each tuple, then the last remaining element of array1 is the answer.
    return array1[-1]
print("{} is the missing number".format(missingElementFinder4([1,2,3,4,5,6,7], [3,7,2,1,5,6])))
