'''
QUESTION -
----------
Write a function which takes the source and destination vertex as arguments and deletes the edge between them if exists.
Example -
Adjacency list: {77: [21], 21: [51, 92], 51: [77], 27: [92], 92: [11], 11: [27, 15]}
src: 11, dest: 27
Result: {77: [21], 21: [51, 92], 51: [77], 27: [92], 92: [11], 11: [15]}

APPROACH -
----------
    1. Check if edge exists between src and dest.
    2. If it does, then remove the vertex = dest from the neighbours of src.
    3. Return -1 if no edge exists between the given src and dest.

TIME COMPLEXITY -
-----------------
O(E) as we look for edge between dest and src from the vertex src.

SPACE COMPLEXITY -
------------------
O(V) as we created adjacency list from the given list of edges.

'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def createAdjList(self, list_of_edges):
        for src, dest in list_of_edges:
            self.adj_list[src].append(dest)

        return self.adj_list

class Solution:
    def removeEdge(self,adj_list,src,dest):
        if dest in adj_list[src]:
            adj_list[src].remove(dest)
            return adj_list
        return -1


if __name__ == '__main__':
    g = Graph()
    edges = [[77,21],[21,51],[21,92],[51,77],[27,92],[92,11],[11,27],[11,15]]
    adj_list = g.createAdjList(edges)
    print(adj_list)

    s = Solution()
    print(s.removeEdge(adj_list, 11,27))
