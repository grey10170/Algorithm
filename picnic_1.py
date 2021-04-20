import sys
rl = lambda: sys.stdin.readline()
n_case = int(rl().strip())


def n_pair(node, edge):
    cnt = 0
    if len(node) == 1:
        return 0
    if len(node) == 0:
        return 1
    del_node = node[0]
    for pair in edge:
        if del_node in pair:
            new_node = []
            for no in node:
                if no not in pair:
                    new_node.append(no)
            new_edge = []
            for new_pair in edge:
                if len(set.intersection(set(pair), set(new_pair))) == 0:
                    new_edge.append(new_pair)
            cnt += n_pair(new_node, new_edge)
    return cnt
for i in range(n_case):
    n_node, n_edge =list(map(int, rl().strip().split(" ")))
    edge = list(map(int, rl().strip().split(" ")))
    edge = list(zip(edge[::2], edge[1::2]))
    assert len(edge) == n_edge
    print(n_pair(list(range(n_node)), edge))