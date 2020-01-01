'''
QUESTION -
----------
https://www.educative.io/courses/data-structures-in-python-an-interview-refresher/qVl6g4PWYEk

Implement a function to find the shortest path between given 2 vertices A and B of the graph. The shortest path is in the terms of number of edges between the two vertices.

Example - 1:
                 70
                 |
                 |
                 |
     10 -------- 50 ---- 40
    /  \          |
   /    \         |
  /      \        |
 20 ---- 30 ---- 60
: (Answer: 2 (20 --- 30 --- 60))

Source: 20
Destination: 60
shortest distance -2

APPROACH -
----------
    1. Perform BFS traversal through the graph.
    2. Initialize a queue with the source vertex and mark that as visited.
    3. Create a default dictionary for maintain the distance between 2 vertices. Its default value is O.
    4. Dequeue vertex from the queue and append all its neighbours to the queue if not visited already.
        - While appending a neigbour to the queue, also capture its distance from the vertex.
        - If while iterating, neighbour of the popped vertex is same as the destination vertex, then return the distance

TIME COMPLEXITY -
------------------
O(V+E) as we traversed through all vertices and edges while performing BFS.

SPACE COMPLEXITY -
------------------
- We used a queue to store the vertices for BFS. There can be at the most O(V) vertices.
- In addition we used visited and distance dicts. Both of these will take O(V) space.

'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def createAdjList(self, list_of_edges):
        for src, dest in list_of_edges:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)

        return self.adj_list

class Solution:
    def shortestPath(self,adj_list,src,dest):
        visited = {}
        q = [src]
        visited[src] = True
        distance = defaultdict(int)

        while q:
            current = q.pop(0)

            for neighbour in adj_list[current]:
                if not visited.get(neighbour):
                    q.append(neighbour)
                    visited[neighbour] = True
                    distance[neighbour] = distance[current] + 1
                    if neighbour == dest:
                        return distance[neighbour]

        return -1


if __name__ == '__main__':
    g = Graph()
    edges = [[77,21],[21,51],[21,92],[51,77],[27,92],[92,11],[11,27],[15,11]]
    adj_list = g.createAdjList(edges)
    print(adj_list)

    s = Solution()
    print(s.shortestPath(adj_list, 77,92))
