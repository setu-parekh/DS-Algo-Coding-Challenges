'''
QUESTION -
----------
For a given graph, perform the DFS traversal and append a vertex to the result list only when it has finished traversing through its destination edges.

APPROACH -
----------
Recursive:
    1. Append the vertex to the visited list.
    2. For the neighbour of that vertex, if it is not in the visited list, recursively call the traversal function with that neighbour.
    3. when all the neighbours of a vertex has been traversed and all present in the visited list, then append that vertex to the result before it return to the function from where it was called.
    4. Once the result list has been populated for the traversal, check whether there is any vertex remaining.
    5. If yes, then call the method by passing that vertex into the function arguement.

TIME COMPLEXITY -
-----------------
O(V+E) as we traversed through all the edges and vertices.

SPACE COMPLEXITY -
------------------
O(V+E) as function call stack is created for vertices and edges.

'''
class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def createAdjList(self, list_of_edges):
        for src, dest in list_of_edges:
            self.adj_list[src].append(dest)

        return self.adj_list

class Solution:
    def modifiedDfs(self, adj_list):
        visited_dict = {} # To keep the track of vertices being visited. If the vertex has been visited, then make it True in the dict.
        result = []

        def dfsUtil(vertex):
            visited_dict[vertex] = True

            for neighbour in adj_list[vertex]:
                if not visited_dict.get(neighbour):
                    dfsUtil(neighbour)

            result.append(vertex)
        # Below iteration makes sure that if there is any disjoint graph, then DFS has been carried out on all the vertices.
        for v in adj_list.keys():
            # If any vertex has not been visited yet, then perform DFS starting from that vertex.
            if not visited_dict.get(v):
                dfsUtil(v)

        return result


if __name__ == '__main__':
    g = Graph()
    edges = [[1,2],[2,3],[3,1],[3,5],[4,5],[5,6],[6,4],[7,6]]
    adj_list = g.createAdjList(edges)
    print(adj_list)

    s = Solution()
    print(s.modifiedDfs(adj_list))
