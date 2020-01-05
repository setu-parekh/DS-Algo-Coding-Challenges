'''
QUESTION -
----------
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

    put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
    Could you do both operations in O(1) time complexity?

Example:

    LRUCache cache = new LRUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4

APPROACH -
----------
Implementing get() and put() in O(1) time can be carried out using OrderedDict():
    - OrderedDict is basically a dict with an additional feature that it remembers the order in which key/   value pairs were added into the dict.
    - This helps us to keep track of the order in which items were added to the dict.
    - Also, we can add, remove (pop) and reorder (move to the end of dict) the items in OrderedDict in O(1) time.
    - For more refrence of OrderedDict, refer to the following links:
        https://www.geeksforgeeks.org/ordereddict-in-python/
        https://docs.python.org/3/library/collections.html#collections.OrderedDict
        https://stackoverflow.com/questions/51800639/complexity-of-deleting-a-key-from-python-ordered-dict

    1. __int__():
        - Initialize a dict to store the key:value pairs as an OrderedDict()
        - We also assign the capacity value to the variable which can be used in other classes.

    2. get():
        - if the desired key is present in the dict, do:
            i. move that key to the end of the dict implying that it has been most recently used.
            ii. return the value of the key.
        - if not present, do:
            i. return -1

    3. put():
        - if the key to be inserted is already present in the dict, do:
            i. move the existing key to the end.
        - Now insert the new key, value pair.
        - After inserting, if the capacity exceeded the specified capacity, do:
            i. pop the 1st pair of the dict. The 1st pair was the least recently used pair.

    Time Complexity -
    ---------------
    - get() and put() operations are O(1) because of OrderedDict().

    Space Complexity -
    ----------------
    - OrderedDict() uses the space upto the specified capacity of the cache, O(N).


'''
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.dict.get(key):
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.dict.get(key):
            self.dict.move_to_end(key)
        self.dict[key] = value
        if len(self.dict.keys()) > self.capacity:
            self.dict.popitem(last = False)


if __name__ == '__main__':
    cache = LRUCache(2)
    print(cache.put(1,1))
    print(cache.put(2,2))
    print(cache.get(1))
    print(cache.put(3,3))
    print(cache.get(1))
    print(cache.put(4,4))
    print(cache.put(5,5))
    print(cache.get(4))
