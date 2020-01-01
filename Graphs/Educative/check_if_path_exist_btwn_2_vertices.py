'''
QUESTION -
----------
https://www.educative.io/courses/data-structures-in-python-an-interview-refresher/gx20Z1kO9lD

Write a function to check whether a path exists between 2 vertices. Consider a source and a destination and check whether path exists between these two.
Note - The path can be direct or indirect.

APPROACH -
----------
    Requirements - Ajdacency list, source, destination

    1. We will check whether the path exists between two vertices using BFS.
    2. Initialize queue with the source vertex and also mark the vertex as visited.
    3. Dequeue the vertex from the queue and append all its neighbours if they have not been visited yet. After appending, mark them visited.
    4. Repeat doing step 3 till the queue is not empty.

TIME COMPLEXITY -
-----------------
O(V+E) as we visited all vertices and edges during BFS.

SPACE COMPLEXITY -
------------------
O(V) as a queue is created for storing vertices and popping.
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
    def checkPath(self,adj_list,src,dest):
        visited = {}
        q = [src]
        visited[src] = True

        while q:
            current = q.pop(0)
            if current == dest:
                return True
            for neighbour in adj_list[current]:
                if not visited.get(neighbour):
                    q.append(neighbour)
                    visited[neighbour] = True

        return False


if __name__ == '__main__':
    g = Graph()
    edges = [[77,21],[21,51],[21,92],[51,77],[27,92],[92,11],[11,27],[15,11]]
    adj_list = g.createAdjList(edges)
    print(adj_list)

    s = Solution()
    print(s.checkPath(adj_list, 77,15))
