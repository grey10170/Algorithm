import sys
import psutil
rl = lambda: sys.stdin.readline()
n_case = int(rl().strip())

def n_pair(n_node, edge, picked):
    cnt = 0
    if sum(picked) == 1:
        return 0
    if sum(picked) == 0:
        return 1
    del_node = picked.index(1)
    for pair in edge:
        if del_node in pair:
            if picked[pair[0]] == 1 and picked[pair[1]] == 1:
                picked[pair[0]], picked[pair[1]] = 0, 0
                cnt += n_pair(n_node, edge, picked)
                picked[pair[0]], picked[pair[1]] = 1, 1
    return cnt
for i in range(n_case):
    n_node, n_edge =list(map(int, rl().strip().split(" ")))
    edge = list(map(int, rl().strip().split(" ")))
    edge = list(zip(edge[::2], edge[1::2]))
    picked = [1 for _ in range(n_node)]
    print(n_pair(n_node, edge, picked))