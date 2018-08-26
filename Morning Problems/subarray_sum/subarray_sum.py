inputsize = int(input())
inputlist = [int(i) for i in input().split()]

currStartVal = -1000000000
currNextVal = 0

for i in range(0, inputsize):
    currNextVal = currNextVal + inputlist[i]
    if currNextVal > currStartVal:
        currStartVal = currNextVal
    if currNextVal < 0:
        currNextVal = 0

if currStartVal < 0:
    currStartVal = 0
print(currStartVal)
