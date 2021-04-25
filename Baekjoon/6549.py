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
    result = max(result, height*2) 
    while left < l or right > r:
        if r< right and (left == l or fence_arr[l-1] < fence_arr[r+1]):
            r += 1
            height = min(height, fence_arr[r])
        else:
            l-= 1
            height = min(height, fence_arr[l])
        result = max(result, height* (r-l+1))
    # print(left, right, result)
    return result
while True:
    length, *fence_arr = list(map(int, rl().split()))
    if length == 0:
        break
    print(getMaxRectangle(0, len(fence_arr)-1))
