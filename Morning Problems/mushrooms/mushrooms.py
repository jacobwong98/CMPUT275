m = int(input())
spots = [int(i) for i in input().split()]
check = spots[0]
low = 0
high = 0

while len(spots) > low:
    if m == 0:
        print(1, end=' ')
        low += 1
    elif high >= len(spots):
        print(0, end=' ')
        low += 1
    elif check < m:
        high += 1
        if high < len(spots):
            check += spots[high]
    else:
        print(high - low + 1, end=' ')
        check -= spots[low]
        low += 1
