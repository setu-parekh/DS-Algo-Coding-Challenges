'''
QUESTION -
https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20PRACTICE/Array%20Pair%20Sum%20.ipynb

APPROACH 1 -
    1. Initializing a dictionary to store pairs whose summation is a specified number.
    2. Initializing a list to store the unique pairs.
    3. Looping through the list of numbers to find a pair whose sum is equal to the specified number. Looping is done 2 number of times.
        i. Outer loop is to consider number of the input list one by one.
        ii. Inner loop is to check whether the 2nd number is same as the 1st one. If not then it is paired with the 1st number considered in the outer loop and checked whether the sum is the specified number.

COMPLEXITY - O(N^2)
'''
# _______________________________________________________________________________________________________
def findSpecificPair(input, sum):
    # dict is in the form: {0:(num_1, num_2)}
    dict = {}
    unique_pair = []
    num_1 = 0
    # Outer loop to fix the 1st position number.
    while num_1 < len(input):
        # Inner loop to check whether the 2nd number is at same position as the 1st. If not then it is checked whether the sum is as required.
        for num_2 in range(len(input)):
            if num_1 != num_2:
                if input[num_1] + input[num_2] == sum:
                    dict[num_1] = (input[num_1], input[num_2])

        num_1 += 1
    # pairs = dict.values()
    # Sorting each value of the key-value pair in the dictionary.
    for i in dict:
        pair = sorted(dict[i])
        # As we want the unique pairs, we will only append those values which are not present in the list - unique_pair.
        if pair not in unique_pair:
            unique_pair.append(pair)
    # Converting list to tuple format.
    for i in range(len(unique_pair)):
        print(tuple(unique_pair[i]))



findSpecificPair([1,3,2,2], 4)
