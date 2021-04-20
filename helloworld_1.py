import sys
rl = lambda: sys.stdin.readline()
n_people = int(rl())
for _ in range(n_people):
    print("Hello, {}!".format(rl().strip()))