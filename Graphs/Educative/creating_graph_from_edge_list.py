'''
QUESTION -
----------
For given list of edges ([source1,destination1], [source2,destination2]), create graph using adjacency list.

APPROACH -
----------
    1. We will create adjacency list using a dictionary.
        key: source vertex
        value: list of destination vertices
'''
from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(list) # while initializing a defaultdict, we have to provide the type of value as the arguement.

    def createAdjLstDirected(self, listOfEdges):
        for source, destination in listOfEdges:
            self.graph[source].append(destination)

        return self.graph

    def createAdjLstUndirected(self, listOfEdges):
        for source, destination in listOfEdges:
            self.graph[source].append(destination)
            self.graph[destination].append(source)

        return self.graph

if __name__ == '__main__':
    s = Solution()
    print(s.createAdjLst([[1,2],[1,3],[1,6],[2,4],[2,6],[3,5],[4,1],[4,3],[4,5],[6,4]]))
    # Output: {1: [2, 3, 6], 2: [4, 6], 3: [5], 4: [1, 3, 5], 6: [4]}
