'''
QUESTION -
----------
https://www.educative.io/courses/data-structures-in-python-an-interview-refresher/7nODy1vm2vj

Find the mother vertex of the graph.

The mother vertex is one from which all other vertices are reachable. It may or may not be directly connected to every vertex, but can reach it through a path traversal. Hence, there can be multiple mother vertices or no mother vertex at all.

     51              27
    /  ^           /   ^
   /    \         /     \
  V      \       V       \
 77 ---> 21 ---> 92 ---> 11 ---> 15
 List of Edges: [[51, 77], [77, 21], [21, 51], [21, 92], [92, 11], [11, 27], [27, 92], [11, 15]]
In the above graph, 51, 77 and 21 are the mother vertices. Because all other vertices can be reached from them.

APPROACH -
----------

Brute Force:

    1. Create a visited and result list. These lists will be reset to empty while performing DFS traversal for each node.
    2. For each vertex in the graph, we will perform the DFS.
        - During each iteration, we will find the length of the traversed/result list.
        - If the length is equal to number of vertices in the graph, then that vertex with which we started the traversal is the mother vertex.

    Time Complexity -
    -----------------
    O(V(V+E)) as we visited all vertices and edges during DFS. Each DFS takes O(V+E) time and We repeated DFS for all total V vertices.

    Space Complexity -
    ------------------
    O(V) used during DFS and for result list.

By finding strongly connected components -

    1. We perform DFS traversal to obtain the vertex which was last in completing its traversal.
        - No need to save the DFS result as we only require the last element of the list.
        - Repeat traversing for each vertex of the graph.
    2. Now after obtaining the last traversed vertex, perform DFS starting from that vertex.
        - maintain the count of each vertex being traversed.
    3. Compare the count and the number of vertices.
        - if they are equal, then the last vertex is the mother vertex.

    Time Complexity -
    -----------------
    O(V+E) as we performed DFS twice:
        1. to obtain the last vertex to finish the traversal.
        2. to traverse the graph starting from the last vertex obtained in the above step.
    Each time the traversal took O(V+E) time.

    Space Complexity -
    ------------------
    O(V) as no space was used apart from DFS.
'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def createAdjList(self, list_of_edges):
        for src, dest in list_of_edges:
            self.adj_list[src].append(dest)

            if not self.adj_list.get(dest):
                self.adj_list[dest] = []

        return self.adj_list

class Solution:
    def bruteForce(self, adj_list):

        def dfsUtil(vertex):
            dfs_visited[vertex] = True
            result.append(vertex)

            for neighbour in adj_list[vertex]:
                if not dfs_visited.get(neighbour):
                    dfsUtil(neighbour)

            return result

        for v in adj_list:
            dfs_visited = {}
            result = []
            single_dfs_run = dfsUtil(v)
            if len(single_dfs_run) == len(adj_list.keys()):
                return True

        return False

    def stronglyConnected(self, adj_list):
        in_order_dfs_visited = {}
        # Initially set the value of last vertex which finished traversing as None. This will be updated after traversing through the entire graph.
        self.last_vertex = None

        def inOrderDfs(vertex):
            in_order_dfs_visited[vertex] = True

            for neighbour in adj_list[vertex]:
                if not in_order_dfs_visited.get(neighbour):
                    inOrderDfs(neighbour)

            self.last_vertex = vertex

        for v in adj_list:
            if not in_order_dfs_visited.get(v):
                inOrderDfs(v)

        self.count = 0
        result = []
        dfs_visited = {}

        def dfs(vertex):
            dfs_visited[vertex] = True
            self.count += 1


            for neighbour in adj_list[vertex]:
                if not dfs_visited.get(neighbour):
                    dfs(neighbour)

            return self.count

        dfs_run = dfs(self.last_vertex)

        if self.count == len(adj_list.keys()):
            return True

        return False


if __name__ == '__main__':
    g = Graph()
    edges = [[77,21],[21,51],[21,92],[51,77],[27,92],[92,11],[11,27],[15,11]]
    adj_list = g.createAdjList(edges)
    print(adj_list)

    s = Solution()
    print(s.bruteForce(adj_list))
    print(s.stronglyConnected(adj_list))
