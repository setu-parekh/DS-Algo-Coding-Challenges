'''
QUESTION -
Implement a function which merges two sorted lists into another sorted list.
Input - Two sorted lists.
Output - A merged and sorted list consisting of all elements of both input lists.

APPROACH 1 -
    1. Initialize pointer for each list.
    2. Create a new list to store the merged sorted elements from both the lists.
    3. Start iterating the list until one of the list is fully iterated.
        i. Compare elements of each list as pointed by the pointers.
            a. Add the smallest of both to the result list and increment the pointer of that same list to check whether the next element is also smaller than the element of other list.
    4. In case of different lengths, check both lists for the remaining element. If remaining, then append those to the result list.
    5. Return result list.

TIME COMPLEXITY - O(N), where N is equal to the number of elements of the bigger list.

APPROACH 2 -
    1. Instead of creating new list, list2 will be merged into list1 and after comparing each element, the resultant list1 will be merged and sorted.
    2. Initialize pointers for each list.
    3. Iterate through both lists till one of them reaches their end.
        i. Compare the elements of the list at the location of the pointers.
            a. If the element of the list2 is smaller than that of list1, then insert the smaller element of list2 in the place of the compared element.
            b. Increment both indices by 1.
            c. If the current element of the list1 is smaller than that of list2, then instead of incrementing both the pointers, increment the pointer of list1 only.
    4. If there are remaining elements in list2, then extend list1 by appending those elements.

TIME COMPLEXITY - O(N*M) ~ O(N^2), where N is equal to the number of elements of the bigger list and M is for insert elements of list2 into list1. While inserting element at a particular position, we have to shift the elements on the right side.
'''

'''
# Approach 1 -

def mergeArrays1(list1, list2):
    merged_list = []
    i = 0 # Pointer for list1
    j = 0 # Pointer for list2
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1 # Incrementing pointer after appending an element to the merged list.
        else:
            merged_list.append(list2[j])
            j += 1 # Incrementing pointer after appending an element to the merged list.
    # Checking whether element is remaining in any list. If yes, then appending those remaining elements to the merged list.
    if i < len(list1):
        merged_list.extend(list1[i:]) # Using extend function to add all the remaning elements to end of the list.
    else:
        merged_list.extend(list2[j:])
    return merged_list
print(mergeArrays1([4,5,7], [1,2,6,8]))
print(mergeArrays1([4], [1,2,3,4,5,6,7]))
print(mergeArrays1([-4,5,7], [-1]))
'''

'''
# Approach 2 -
def mergeArrays2(list1, list2):
    i = 0 # Pointer for list1
    j = 0 # Pointer for list2
    # Iterating till elements in one of list reaches to end.
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            list1.insert(i, list2[j]) # Inserting the smaller element of list2 in the place of existing bigger element with which it was compared.
            i += 1
            j += 1
        else:
            i += 1
    # Extending the list1 with remaining elements of list2.
    if j < len(list2):
        list1.extend(list2[j:])
    return list1
print(mergeArrays2([4,5,7], [1,2,6,8]))
print(mergeArrays2([4], [1,2,3,4,5,6,7]))
print(mergeArrays2([-4,5,7], [-1]))
'''
