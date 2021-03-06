class DepthFirstSearch:
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.adj_list = [[] for _ in range(self.n)]

    # Edge数分回すことを想定
    def add_edge(self, start, end, undirected=True):
        self.adj_list[start].append(end)
        if undirected:
            self.adj_list[end].append(start)

    def search(self, start_node):
        preorder = [-1] * self.n  # a dfs preordering of each vertex
        postorder = [-1] * self.n  # a dfs postordering of each vertex
        parent = [-1] * self.n  # parent of each vertex in the dfs search tree
        depth = [-1] * self.n  # the depth of each vertex
        stack = [(start_node, -1, 0)]  # (vertex, parent, status)
        pre_num = 0  # current preordering
        post_num = 0  # current postordering
        d = 0  # current depth
        while len(stack) > 0:
            v, p, st = stack.pop()
            if st == 0 and preorder[v] < 0:  # visited v for the first time
                preorder[v] = pre_num
                parent[v] = p
                depth[v] = d
                pre_num += 1
                n_children = 0
                for u in self.adj_list[v]:
                    if preorder[u] >= 0:
                        continue
                    if n_children == 0:
                        stack += [(v, p, 2), (u, v, 0)]
                        n_children += 1
                    else:
                        stack += [(v, p, 1), (u, v, 0)]
                        n_children += 1
                if n_children == 0:  # v is a leaf
                    postorder[v] = post_num
                    post_num += 1
                    d -= 1
                else:
                    d += 1
            elif st == 0 and preorder[v] >= 0:  # the edge (v, p) is a back edge
                d -= 1
            elif st == 1:  # now searching
                d += 1
            else:  # search finished (st=2)
                postorder[v] = post_num
                post_num += 1
                d -= 1
        return preorder, postorder, parent, depth


# 重みなしグラフの隣接リスト
# 0-indexed nodes
def get_adj_list(num_nodes, data, undirected=True):
    graph = [[] for _ in range(num_nodes)]
    for val in data:
        x, y = val
        graph[x].append(y)
        if undirected:
            graph[y].append(x)
    return graph


# DFS
# preorder : 頂点に初めてたどり着いた時刻
# preorder : その頂点の全ての辺を探索し終えた時刻
def depth_first_search(adj_list, start_node):
    N = len(adj_list)
    preorder = [-1] * N  # a dfs preordering of each vertex
    postorder = [-1] * N  # a dfs postordering of each vertex
    parent = [-1] * N  # parent of each vertex in the dfs search tree
    depth = [-1] * N  # the depth of each vertex
    stack = [(start_node, -1, 0)]  # (vertex, parent, status)
    pre_num = 0  # current preordering
    post_num = 0  # current postordering
    d = 0  # current depth
    while len(stack) > 0:
        v, p, st = stack.pop()
        if st == 0 and preorder[v] < 0:  # visited v for the first time
            preorder[v] = pre_num
            parent[v] = p
            depth[v] = d
            pre_num += 1
            n_children = 0
            for u in adj_list[v]:
                if preorder[u] >= 0:
                    continue
                if n_children == 0:
                    stack += [(v, p, 2), (u, v, 0)]
                    n_children += 1
                else:
                    stack += [(v, p, 1), (u, v, 0)]
                    n_children += 1
            if n_children == 0:  # v is a leaf
                postorder[v] = post_num
                post_num += 1
                d -= 1
            else:
                d += 1
        elif st == 0 and preorder[v] >= 0:  # the edge (v, p) is a back edge
            d -= 1
        elif st == 1:  # now searching
            d += 1
        else:  # search finished (st=2)
            postorder[v] = post_num
            post_num += 1
            d -= 1
    return preorder, postorder, parent, depth
