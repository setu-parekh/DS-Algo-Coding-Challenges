from collections import defaultdict


class Solution:
    def __init__(self, adj_list):
        self.adj_lst = adj_list

    def reverseGraph(self):
        reversed_adj_list = defaultdict(list)
        for v in self.adj_lst.keys():
            for neighbour in adj_list[v]:
                reversed_adj_list[neighbour].append(v)

        return reversed_adj_list


if __name__ == '__main__':
    adj_list = {1: [2, 3, 6], 2: [4, 6], 3: [5], 4: [1, 3, 5], 6: [4]}
    s = Solution(adj_list)
    print(s.reverseGraph())
