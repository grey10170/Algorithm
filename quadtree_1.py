import sys
rl = sys.stdin.readline

def tree2Code(quad_tree):
    code = []
    for i in quad_tree[::-1]:
        if i=='x' or i=='b' or i=='w':
            code.append(i)
        else:
            code+= tree2Code(i)
    return ''.join(code)
'''
Tree 구조를 다시 얻기 위해 역순으로 보고,
x를 통해서 묶어나간다. 이때, 역순까지 한번에 처리
이후 다시 Tree2Code를 이용해서 Code로 변환한다.
이때 역시 역순을 고려한다.
'''
def quadVerticalFlip(quad_code):
    quad_parse = [i for i in quad_code[::-1]]
    while 'x' in quad_parse:
        idx = quad_parse.index('x')
        tree = [quad_parse[idx-2], quad_parse[idx-1], quad_parse[idx-4], quad_parse[idx-3], quad_parse[idx]]
        quad_parse.insert(idx+1, tree)
        del quad_parse[idx-4:idx+1]
    return tree2Code(quad_parse)


n_case = int(rl())
for _ in range(n_case):
    quad_code = rl().strip()
    print(quadVerticalFlip(quad_code))
