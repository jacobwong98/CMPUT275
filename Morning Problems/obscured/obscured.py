heights = [int(i) for i in input().split()]

maxh = -1
maxi = -1
result = []

for i, h in enumerate(heights):
    if h > maxh:
        maxh = h
        maxi = i
        result.append('X')
    elif h < heights[i-1]:
        result.append(i-1)
    else:
        a = i-1
        while heights[a] < h:
            a = result[a]
        result.append(a)
print(*result)
