'''
QUESTION -
https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20PRACTICE/String%20Compression%20.ipynb

APPROACH 1 -
    1. Compressing the string by creating a dictionary and storing each element with its corresponding count.
    2. Initializing an empty string and concatenating it with key and its count value.

APPROACH 2 -
    1. Initializing count and index counter to 1. Incrementing the counter by comparing each element with its previous one.
    2. If both are equal, then concatenating the element with its corresponding count to the string.
    3. Once this is done for a particular element, resetting the counter back to 1.

TIME COMPLEXITY -
    1. Approach 1 - O(N)
    2. Approach 2 - O(N)

'''
# ________________________________________________________________________________________________________
# Approach 1 -
'''
# Defining a method to compress the given string by creating a dictionary for storing each element and its count.
def stringCompression1(string):
    count_dict = {}
    compressed_string = ' '
    for alpha in string:
        if alpha not in count_dict:
            count_dict[alpha] = 1
        else:
            count_dict[alpha] += 1
    # Iterating to concatenate key and value of the dictionary to form a compressed string.
    for key in count_dict.keys():
        compressed_string = compressed_string + key + str(count_dict[key])
    return compressed_string
print(stringCompression1("AABBB")) # Output - A2B3
print(stringCompression1("ABBBC")) # Output - A1B3C1
print(stringCompression1("A"))     # Output - A1
print(stringCompression1(""))
print(stringCompression1("aaBb"))
'''
#________________________________________________________________________________________________________
# Approach 2 -
'''
# Defining a method to compress string to count the alphabet repeatation at each step by comparing with the previous element and concatenating to a string simultaneously.
def stringCompression2(string):
    compressed_string = " "
    # Testing edge case when the provided string does not contain any element.
    if len(string) == 0:
        return " "
    # Testing edge case when the provided string contains only 1 element.
    if len(string) == 1:
        return string + '1'
    # Starting the index counter from 1 as we will compare with the previous element, i-1.
    # If we start from i = 0, then it will provide range error as we will compare with the next element and when counter reaches the last element of the string, there will be no element at i+1.
    i = 1
    count = 1
    while i < len(string):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed_string = compressed_string + string[i-1] + str(count)
            count = 1 # Resetting count to 1 again as we encounted a new element.
        i = i + 1
    compressed_string = compressed_string + string[i-1] + str(count)
    return compressed_string

print(stringCompression2("AABBB")) # Output - A2B3
print(stringCompression2("ABBBC")) # Output - A1B3C1
print(stringCompression2("A"))     # Output - A1
print(stringCompression2(""))
print(stringCompression2("aaBb"))
'''
