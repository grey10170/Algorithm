import sys
import math
rl = sys.stdin.readline

N = int(rl())
points =[] 

def getDist(point1, point2):
    return (point1[0]- point2[0])**2 + (point1[1]- point2[1])**2

def getMinDist(left, right):
    length = right-left
    if length ==0:
        return float('inf')
    center = (right+ left)//2
    x_div = points[center][0]
    dist = min(getMinDist(left, center), getMinDist(center+1, right))
    l = center
    while  l>= 0 and points[l][0] >= x_div -dist:
        r= center +1
        while r <= right and points[r][0]- points[l][0] <= dist:
            dist = min(getDist(points[l], points[r]), dist)
            r += 1
        l -= 1
    r = center+1
    while r <= right and points[r][0] >= x_div +dist :
        l = center
        while l>= 0 and points[r][0]- points[l][0] <= dist:
            dist = min(getDist(points[l], points[r]), dist)
            l -= 1
        r += 1
    return dist

for _ in range(N):
    points.append(list(map(int, rl().split())))
points.sort(key= lambda x: x[0])
# print(points)
print(getMinDist(0, N-1))