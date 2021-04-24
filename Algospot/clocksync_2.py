import sys

rl = sys.stdin.readline

switches = [
    [0, 1, 2],
    [3, 7, 9, 11], #11
    [4, 10, 14, 15], #10
    [0, 4, 5, 6, 7], #6
    [6, 7, 8, 10, 12], #12, 8
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13] #13
]
MAX, N_CLOCK, N_SWITCH = 1000, 16, 10

def nSwitchNeed_(start,remain, init_clock):
    if any(init_clock) == False:
        return 0
    if start >= len(remain):
        return MAX
    min_ = MAX
    for n_start_pressed in range(4):
        min_ = min(min_, nSwitchNeed_(start+1,remain, init_clock)+n_start_pressed) 
        for i in switches[remain[start]]:
            init_clock[i] = (init_clock[i]+1)%4
    return min_

def nSwitchNeed(init_clock):
    n_press = [0 for i in range(N_SWITCH)]
    #13
    n_press[9]= (4-init_clock[13])%4
    for i in switches[9]:
        init_clock[i] = (n_press[9] + init_clock[i])%4
    #12
    n_press[4]= (4-init_clock[12])%4
    for i in switches[4]:
        init_clock[i] = (n_press[4] + init_clock[i])%4
    #11
    n_press[1]= (4-init_clock[11])%4
    for i in switches[1]:
        init_clock[i] = (n_press[1] + init_clock[i])%4
    #10
    n_press[2]= (4-init_clock[10])%4
    for i in switches[2]:
        init_clock[i] = (n_press[2] + init_clock[i])%4
    #6
    n_press[3]= (4-init_clock[6])%4
    for i in switches[3]:
        init_clock[i] = (n_press[3] + init_clock[i])%4
    remain = [0,5,6,7,8]
    cnt = nSwitchNeed_(0, remain, init_clock)
    cnt += n_press[1]+ n_press[2]+ n_press[3]+ n_press[4]+ n_press[9]
    return cnt

n_case = int(rl())
for _ in range(n_case):
    init_clock = list(map(lambda x: (int(x)//3)%4, rl().split()))
    result = nSwitchNeed(init_clock)
    if result >= MAX:
        result = -1
    print(result)