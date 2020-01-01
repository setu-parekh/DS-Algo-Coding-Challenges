'''
QUESTION -
Given a list and a number "n", find two numbers from the list that sum to "n".
Input - A list and a number n
Output - A list with two integers a and b that add up to n

APPROACH 1 -
    1. Initialize 2 pointers for the list at index 0 and 1.
    2. Keeping the 1st pointer at its position, iterate the 2nd pointer through the list.
    3. Add the elements corresponding to the pointer locations and compare the sum with the given value.
        i. if the sum matches the given value, then return the values corresponding to both pointers.
        ii. if the sum does not match with the given value, increment the 2nd pointer first and when it comes to the end, increment the 1st pointer.

    TIME COMPLEXITY - O(N^2)

APPROACH 2 -
    1. First sorting the list.
    2. Initializing 2 indices for first and last element of the list.
    3. Iterating the list by incrementing the first element and decrementing the last element till a middle        point is reached.
        i. During each iteration, adding the integers at both pointers.
        ii. Comparing the sum with the provided value. If the sum is less than the value, incrementing the pointer at the starting of the list.
        iii. If the sum is greater than the value, decrementing the pointer at the end of the list.

    TIME COMPLEXITY - sorting takes O(Nlog(N)) and iterating through the list from both end take O(N). Overall complexity is O(Nlog(N)).

APPROACH 3 -
    1. Create an empty dictionary to store each element of the list along with its index.
    2. Iterating through the list
        i. subtracting the element from the given sum.
        ii. check whether the resultant value is in the dictionary. If present, then return element, sum - element.
        iii. If the resultant value is not present in the dictionary, store the element in the dictionary.

    TIME COMPLEXITY - O(N) as dict.get() is of order O(1).

APPROACH 4 -
    1. Create an empty set.
    2. Iterate through the list.
        i. Find difference between the sum and element during each iteration.
        ii. Search for the difference value in the set.
        iii. If not found, then add the element to the set and if found, return element, sum - element.

    TIME COMPLEXITY - O(N) as search in set() is of order O(1).

'''
# __________________________________________________________________________________________________________________
'''
# Approach 1 -

def findSum1(list, givenSum):
    i = 0 # Initializing at index = 0
    j = 1 # Initializing at index = 1
    while i < len(list): # Outer iteration loop
        while j < len(list): # Inner iteration loop
            if list[i] + list[j] == givenSum:
                return [list[i], list[j]]
            else:
                j += 1
        i += 1 # Incrementing i when inner iteration loop ends once.
        j = i + 1 # Shifting the position of j next to i.
print(findSum1([1,21,3,14,5,60,7,6], 81))
'''
# __________________________________________________________________________________________________________________
# Approach 2 -
'''
def findSum2(list, givenSum):
    list.sort()
    start = 0 # Initializing start index
    end = len(list) - 1 # Initializing the index of last element of the list by finding the length of the list and subtacting 1 from it as index starts from 0.
    while list[start] != list[end]:
        if list[start] + list[end] > givenSum:
            end = end - 1
        elif list[start] + list[end] < givenSum:
            start = start + 1
        else:
            return [list[start], list[end]]
    return False

if __name__ == '__main__':
    print(findSum2([1,21,-3,14,-5,60,7,6], 81))
'''
#__________________________________________________________________________________________________________________
# Approach 3 -

def findSum3(nums, target):
    visited = {}
    i = 0

    while i < len(nums):
        complement_num = target - nums[i]
        if visited.get(complement_num):
            return [i,visited[complement_num]]
        else:
            visited[nums[i]] = i

        i += 1
    return []

    # num_dict = {}
    # for i in range(len(list)):
    #     if num_dict.get(givenSum - list[i]) is not None:  # get()is used to achieve O(1) search operation.
    #         return [list[i], givenSum - list[i]]
    #     else:
    #         num_dict[list[i]] = i

if __name__ == '__main__': # This is the syntax to start executing from the main method.
    print(findSum3([1,21,-3,14,-5,60,7,6], 81))

#__________________________________________________________________________________________________________________
# Approach 4 -
'''
def findSum4(list, givenSum):
    num_set = set() # Advantage of using set over list is that it is in the order of O(1) while searching for any element in the set. Just like dict.get() function.
    for element in list:
        difference = givenSum - element
        if difference in num_set:
            return [element, difference]
        else:
            num_set.add(element)
        # print(num_set)
    return False

if __name__ == '__main__':
    print(findSum4([1,21,-3,14,-5,60,7,6], 81))
'''
