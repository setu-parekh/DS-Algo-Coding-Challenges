'''
QUESTION -
----------
Write a function to check whether the given graph is tree or not.
A graph is said to be tree if -
    - It does not contain any cycles.
    - All vertices are connected or the graph is connected.

In a connected graph, there is no unreachable vertices. Every vertex can be reached through either direct or indirect vertex through graph traversal.

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
    def checkTree(self, adj_list):
        visited = {}
        rec_stack =[]

        def checkTreeUtil(vertex):
            visited[vertex] = True
            # rec_stack.append(vertex)

            for neighbour in adj_list[vertex]:
                if neighbour in rec_stack:
                    return True
                elif not visited.get(neighbour):
                    if checkTreeUtil(neighbour):
                        return True
            return False

        # if checkTreeUtil(0):
        #     return False

        for v in adj_list.keys():

            rec_stack = []
            if not visited.get(v):
                if checkTreeUtil(v):
                    return False

        # if len(adj_list.keys()) != len(visited.keys()):
        #     return False

        return True

if __name__ == '__main__':
    g = Graph()
    edges = [[0,1],[0,2],[0,3],[3,4]]
    adj_list = g.createAdjList(edges)
    print(adj_list)

    s = Solution()
    print(s.checkTree(adj_list))
