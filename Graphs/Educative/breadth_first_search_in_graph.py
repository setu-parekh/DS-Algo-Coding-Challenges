'''
QUESTION -
----------
Write a program to perform breadth first search in a graph.

APPROACH -
----------
    1. Create a queue and visited list initialized with the start node.
    2. Create an empty result list.
    3. Iterate through the queue till it is not empty:
        - pop the first element of the queue and append it to the result list.
        - iterate through the edge list corresponding to the popped element in dict.
            - if the element of the edge list in not present in the visited list, then append it to queue as well as visited list.
    4. Return result list.

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

    def bfs(self, node):
        self.queue = [node]
        self.visited = [node]
        self.result = []

        while self.queue:
            current = self.queue.pop(0)
            self.result.append(current)
            for element in self.graph[current]:
                if element not in self.visited:
                    self.queue.append(element)
                    self.visited.append(element)
        return self.result

if __name__ == '__main__':
    s = Solution()
    print(s.createAdjLst([[1,2],[1,3],[1,6],[2,4],[2,6],[3,5],[4,1],[4,3],[4,5],[6,4]]))
    print(s.bfs(1))
