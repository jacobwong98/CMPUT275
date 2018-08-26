import itertools
numCand = int(input())
listCand = [int(i) for i in input().split()]
sumCand = sum(listCand)

sizeSum = sumCand/2

combination = [k for i in range(numCand, 0, -1) for k in itertools.combinations(listCand, i) if sum(k) == sizeSum]

if combination:
    print(True)
else:
    print(False)
