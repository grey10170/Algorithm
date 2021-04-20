import sys
rl = lambda: sys.stdin.readline()
n_case = int(rl())

def countMatching(nodes, edges, matched):
    if False in matched:
        target = matched.index(False)
    else:
        return 1
    cnt = 0
    for node in range(target+1, nodes):
        if not matched[node]:
            if edges[target][node]:
                matched[target]= matched[node]= True
                cnt += countMatching(nodes, edges, matched)
                matched[target]= matched[node]= False
    return cnt
        
for _ in range(n_case):
    n_people, n_edge = map(int, rl().split())

    edges_idx= list(map(int, rl().split()))
    matched = [False]*n_people
    edges = [[False]*n_people for _ in range(n_people)]
    for i in range(n_edge):
        edges[edges_idx[2*i]][edges_idx[2*i+1]] = True
        edges[edges_idx[2*i+1]][edges_idx[2*i]] = True

    print(countMatching(n_people,edges, matched))
