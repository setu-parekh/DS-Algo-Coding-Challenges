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

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def createAdjLst(self, listOfEdges):
        for source, destination in listOfEdges:
            self.graph[source].append(destination)

        return self.graph

    def dfsRecursive(self,start):
        if start is None: # Edge Case
            return []

        self.visited = [] # Creating visited list to maintain the track of visited vertices so that they are not visited more than once.
        self.result = []

        def dfsHelper(node):
            self.result.append(node)
            self.visited.append(node)

            for element in self.graph[node]:
                if element not in self.visited:
                    dfsHelper(element) # Recursive call to the neighbour of the vertex

        dfsHelper(start)
        return self.result

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
    s = Solution()
    # print(s.createAdjLst([[1,2],[1,3],[1,6],[2,4],[2,6],[3,5],[4,1],[4,3],[4,5],[6,4]]))
    print(s.createAdjLst([[1,2],[1,3],[2,5],[2,4],[3,5],[4,6],[5,6],[6,7]]))
    print(s.dfsRecursive(1))
    print(s.dfsIterative(1))
