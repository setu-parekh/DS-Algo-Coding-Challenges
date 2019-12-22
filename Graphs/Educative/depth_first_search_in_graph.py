'''
QUESTION -
----------
Write a program to perform depth first search of a graph from given list of edges.

APPROACH -
-----------
    1. Initialize graph as a defaultdict where vertices are the keys and list of their destination vertices as values.
    2. Populate defaultdict with keys and values to create graph.
    3. For DFS, create visited and result list.
    4. For elements in the list of each key: append them to result and visited list, if that element is not already present in the visited list.

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

    def dfs(self,start):
        if start is None:
            return []
        self.visited = []
        self.result = []

        def dfsHelper(node):
            self.result.append(node)
            self.visited.append(node)

            for element in self.graph[node]:
                if element not in self.visited:
                    dfsHelper(element)

        dfsHelper(start)
        return self.result

if __name__ == '__main__':
    s = Solution()
    print(s.createAdjLst([[1,2],[1,3],[1,6],[2,4],[2,6],[3,5],[4,1],[4,3],[4,5],[6,4]]))
    print(s.dfs(1))
