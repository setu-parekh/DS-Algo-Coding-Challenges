'''
QUESTION -
----------
Detect a cycle if any in the graph. Return True if present and False if absent.

APPROACH -
----------
Requirements -
    1. A dictionary to store visited vertices. If a vertex has been visited, then the value corresponding to that is True.
    2. A recurrsion stack to store vertices for each DFS. During a particular DFS run, if we come across a vertex which is already present in the recurrsion stack, this implies that a cycle is present.
    Recurrsion stack is reset to empty after each DFS cycle.

Pseudo Code -

    Utility function -

    1. Starting from a vertex, first mark that vertex as True in the visited dictionary. Append it to the recurrsion stack.
    2. Move on to the neighbour of the vertex.
        Case 1:
        -------
        - if that neighbour is already in the recursion stack, then return True as a cycle exists.
        Case 2:
        -------
        - if that neighbour is not present in the visited dict, then call the method using that neighbour.
            - If after calling that method, the vertex is present, in the rec_stack, then return True

    Main function -

    1. Iterate over all the vertices of the graph, to ensure that dfs covers all of them. In this way, we can take care of the disjoint graph.
    2. Recursion stack for each DFS run should be initially empty.
    3. Call the utility function to detect the cycle on the vertex if it has not been visited yet.
    4. If that function returns True, then no need to iterate over the rest vertices.

TIME COMPLEXITY -
-----------------
O(V+E) as we traversed through all the vertices and edges of the graph.

SPACE COMPLEXITY -
------------------
O(V+E) as a function call stack is created for all the vertices and edges.


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
    def isCycle(self, adj_list):
        visited = {}

        def isCycleUtil(vertex):
            visited[vertex] = True
            rec_stack.append(vertex)

            for neighbour in adj_list[vertex]:
                if neighbour in rec_stack:
                    return True
                elif visited.get(neighbour) == None:
                    isCycleUtil(neighbour)
                    if isCycleUtil(neighbour):
                        return True
                # Above elif can be concised as this:
                # elif (not visited.get(neighbour) and isCycleUtil(neighbour)):
                #   return True

            return False

        for v in adj_list.keys():
            rec_stack = []
            # Above two if conditions can be combined into one as:
            # if not visited.get(v) and isCycleUtil(v):
            #   return True

            if not visited.get(v):
                if isCycleUtil(v):
                    return True

        return False


if __name__ == '__main__':
    g = Graph()
    edges = [[12,22],[22,7],[7,12],[7,19],[19,15],[15,6],[6,19],[3,15]]
    adj_list = g.createAdjList(edges)

    s = Solution()
    print(s.isCycle(adj_list))
