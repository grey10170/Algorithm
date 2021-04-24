import sys

rl = sys.stdin.readline

fence_arr =[]

def getMaxRectangle(left, right):
    if right==left:
        return fence_arr[left]
    center = (left+right) //2
    result = max(getMaxRectangle(left, center), getMaxRectangle(center+1, right))
    l, r = center, center+1
    height = min(fence_arr[l], fence_arr[r]) 
    while left < l or right > r:
        if r< right and (left == l or fence_arr[l-1] < fence_arr[r+1]):
            r += 1
            height = min(height, fence_arr[r])
        else:
            l-= 1
            height = min(height, fence_arr[l])
        result = max(result, height* (r-l+1))
    return result

n_case = int(rl())
for _ in range(n_case):
    arr_len = int(rl())
    fence_arr = list(map(int, rl().split()))
    print(getMaxRectangle(0, arr_len-1))
