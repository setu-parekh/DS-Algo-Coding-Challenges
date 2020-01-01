from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def createAdjList(self, list_of_edges):
        for src, dest in list_of_edges:
            self.adj_list[src].append(dest)

        return self.adj_list

class Solution:
    # Method to find strongly connected components of a given graph.
    def strongly_connected_components(self, adj_list):
        in_order_dfs_visited = {}
        iteration_list = [] # List containing vertices who got finished traversing in order.
        reversed_dfs_visited = {}
        result = [] # List of strongly connected vertices.

        # Method to performing DFS on the given graph and preparing a list in the order of vertices finishing their traversal first.
        def dfsInOrderUtil(vertex):
            in_order_dfs_visited[vertex] = True

            for neighbour in adj_list[vertex]:
                if not in_order_dfs_visited.get(neighbour):
                    dfsInOrderUtil(neighbour)

            iteration_list.append(vertex)

        # Method to reverse the edges of the given graph
        def reverseGraph(adj_list):
            reverse = defaultdict(list)
            for k in adj_list.keys():
                for neighbour in adj_list[k]:
                    reverse[neighbour].append(k)
            return reverse

        reversed_adj_list = reverseGraph(adj_list)

        # Method to perform DFS on the reversed graph and obtaining the list of strongly connected vertices.
        def reverseGraphDfsUtil(vertex):
            reversed_dfs_visited[vertex] = True
            connected_comp_set.append(vertex)

            for neighbour in reversed_adj_list[vertex]:
                if not reversed_dfs_visited.get(neighbour):
                    reverseGraphDfsUtil(neighbour)

        # Iterating through all the vertices and recursively calling the method to obtain list of vertices in order of their traversal completition.
        #Vertices are considered only if they have not been visited yet.
        for v in adj_list.keys():
            if not dfs_visited.get(v):
                dfsInOrderUtil(v)

        # After obtaining the list, perform DFS on the reversed graph starting from the popped vertex from the list.
        # Recursively call the method for DFS in reversed graph. Call the method only if the starting vertex is not present in the visited list.
        # Reset the strongly connected vertex list to empty after each iteration.
        # Append each set of strongly connected vertex to the result list.
        while iteration_list:
            connected_comp_set = []
            v = iteration_list.pop()
            if not reversed_dfs_visited.get(v):
                reverseGraphDfsUtil(v)
            else:
                continue
            result.append(connected_comp_set)

        return result


if __name__ == '__main__':
    g = Graph()
    edges = [[1,2],[2,3],[3,1],[3,5],[4,5],[5,6],[6,4],[7,6]]
    adj_list = g.createAdjList(edges)

    s = Solution()
    print(s.strongly_connected_components(adj_list))
