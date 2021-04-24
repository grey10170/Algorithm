import sys
rl = sys.stdin.readline

n_case = int(rl())

def getMaxRectangle(fence_arr):
    length = len(fence_arr)
    center = length//2
    if length == 1:
        return fence_arr[0]
    result = max(getMaxRectangle(fence_arr[:center]),getMaxRectangle(fence_arr[center:]))
    left_idx, right_idx = center-1, center
    height = min(fence_arr[center-1], fence_arr[center])
    while left_idx >=0 and right_idx< length:
        if left_idx ==0 and right_idx< length-1:
            height = min(fence_arr[right_idx+1],height)
            right_idx +=1
        elif right_idx< length-1 and fence_arr[left_idx-1] > fence_arr[right_idx+1]:
            height = min(fence_arr[left_idx-1],height)
            left_idx -=1
        elif right_idx< length-1 and fence_arr[left_idx-1] <= fence_arr[right_idx+1]:
            height = min(fence_arr[right_idx+1],height)
            right_idx +=1
        elif right_idx ==length-1 and left_idx>0:
            height = min(fence_arr[left_idx-1],height)
            left_idx -=1
        else:
            break
        result = max(result, height*(right_idx-left_idx+1))
    
        
    return result


for _ in range(n_case):
    n_fence = int(rl())
    fence_arr = list(map(int, rl().split()))
    print(getMaxRectangle(fence_arr))
