'''
QUESTION -
----------
Write a program to perform depth first search of a graph from given list of edges.

APPROACH -
-----------
Recursive:
    1. For DFS, create visited and result list.
    2. Starting from the given input vertex, dive deep down till we reach the deadend.
    3. Backtrack from where the function call was made and explore any unexplored neighbour for that vertex.

Iterative:
    1. Initialize stack with start vertex.
    2. Create visited list
    3. Pop the vertex from the stack
    4. Append vertex to visited list if that vertex is not already present. If present, then simply continue popping the next top vertex from the stack.
    5. Push neighbours of popped vertex on to the stack.

TIME COMPLEXITY -
-----------------
O(V+E) where V is number of vertices and E is number of edges as we traversed through all the vertices and edges between them.

SPACE COMPLEXITY -
------------------
O(V+E) as function call stack is created for vertices and edges.

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
    def dfsRecursive(self, adj_list):
        visited_dict = {} # To keep the track of vertices being visited. If the vertex has been visited, then make it True in the dict.
        result = []

        def dfsUtil(vertex):
            visited_dict[vertex] = True
            result.append(vertex)

            for neighbour in adj_list[vertex]:
                if not visited_dict.get(neighbour):
                    dfsUtil(neighbour)
        # Below iteration makes sure that if there is any disjoint graph, then DFS has been carried out on all the vertices.
        for v in adj_list.keys():
            # If any vertex has not been visited yet, then perform DFS starting from that vertex.
            if not visited_dict.get(v):
                dfsUtil(v)

        return result

    def dfsIterative(self, start):
        # Initialize stack with the start node
        stack = [start]
        # create empty visited list to keep the track of visited vertices so that they are not visited again.
        visited = []
        # Iterating till the stack is not empty:
        while stack:
            vertex = stack.pop()
            # Appending the vertex to the visited list if not present already. If present, then continue popping next vertex.
            if vertex not in visited:
                visited.append(vertex)
            else:
                continue
            # Pushing the neighbors of the vertex on to the stack.
            for neighbor in self.graph[vertex]:
                stack.append(neighbor)

        return visited

if __name__ == '__main__':
    g = Graph()
    edges = [[12,22],[22,7],[7,12],[7,19],[19,15],[15,6],[6,19],[3,15]]
    adj_list = g.createAdjList(edges)
    print(adj_list)

    s = Solution()
    print(s.dfsRecursive(adj_list))
