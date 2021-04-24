import sys

rl = sys.stdin.readline

switches = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]
MAX, N_CLOCK, N_SWITCH = 1000, 16, 10


def nSwitchNeed(start, init_clock):
    if any(init_clock) == False:
        return 0
    if start >= N_SWITCH:
        return MAX
    min_ = MAX
    for n_start_pressed in range(4):
        min_ = min(min_, nSwitchNeed(start+1, init_clock)+n_start_pressed) 
        for i in switches[start]:
            init_clock[i] = (init_clock[i]+1)%4
    return min_

n_case = int(rl())
for _ in range(n_case):
    init_clock = list(map(lambda x: (int(x)//3)%4, rl().split()))
    result = nSwitchNeed(0, init_clock)
    if result == MAX:
        result = -1
    print(result)