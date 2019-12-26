import heapq as hq
'''
heappush()
---------
- adds element to the heap. Resultant Heap is the min Heap
Note - Don’t apply it on any old list, instead use the one that you built using Heap functions. That is how you can ensure the elements are in the desired order.
'''
num_list = [10,50,40,70,20,4,100]
heap = []
for num in num_list:
    hq.heappush(heap,num)
print("Heap list:", heap)
hq.heappush(heap,0)
print("Heap after adding new element:", heap)

'''
heappop()
---------
- removes smallest element from the min Heap.
'''
print("Smallest element of the heap", hq.heappop(heap))
print("Next smallest element of the heap", hq.heappop(heap))
print("Next smallest element of the heap", hq.heappop(heap))

'''
heappushpop()
-------------
- This first adds new element to the heap and then pops the smallest element.
- Pushing new node - 95 to the heap and popping the smallest.
'''
popped_min_node = hq.heappushpop(heap,95)
print(heap)

'''
heapify()
- This function accepts some random list and then converts it into a heap.
'''
raw_list = [4,1,9,12,45,63,2,0]
hq.heapify(raw_list)
print("Heapified list:", raw_list)

'''
heapreplace()
-------------
- This function deletes the smallest node and then inserts the new node. It is more efficient than heappop() and heappush()
- We will use the above heapified raw list as an example.
'''
hq.heapreplace(raw_list, 10)
print("Heap after heapreplace():", raw_list )

'''
nlargest()
----------
- First of all, convert the list into a max heap.

- It finds the n largest elements from a given iterable. It also accepts a key which is a function of one argument.

- The selected items have to satisfy the k function. If any of them fails, then the next higher number is considered.

- From the given heapified raw_list, Find 2 largest numbers. Output is the list of largest numbers.
'''

# To apply max functions to heap, first convert the BT into a max heap
binaryTree = [9, 11, 13, 34, 45, 80, 99, 78]
hq._heapify_max(binaryTree)
print("Max heap:", binaryTree)

two_largest = hq.nlargest(2, binaryTree, key = None)
print("Two largest nodes are:", two_largest)

# Writing a program using key.
def isEven(num):
    if num%2 == 0:
        return 1
    return 0

two_even_largest = hq.nlargest(2, binaryTree, isEven)
print("Two even largest nodes are:", two_even_largest)

'''
nsmallest()
----------
- It finds the n largest elements from a given iterable. It also accepts a key which is a function of one argument.

- The selected items have to satisfy the k function. If any of them fails, then the next higher number is considered.

- From the given heapified raw_list, Find 2 largest numbers. Output is the list of largest numbers.
'''
input_list = [9, 11, 13, 34, 45, 80, 99, 78]
hq.heapify(input_list)

two_smallest = hq.nsmallest(2, input_list, key = None)
print("Two smallest nodes are:", two_smallest)

# Writing a program using key.
def isEven(num):
    if num%2 == 0:
        return 1
    return 0

two_even_smallest = hq.nsmallest(2, input_list, isEven)
print("Two even smallest nodes are:", two_even_smallest)
