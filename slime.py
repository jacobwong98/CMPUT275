# read the input
size = int(input())
slimes = []

# solve the problem
for i in range(0,size):
    slimes.append(1)
    while len(slimes) > 1 and slimes[-1] is slimes[-2]:
        slimes.pop()
        slimes.append(slimes.pop() + 1)
# print the answer
print(' '.join(str(i) for i in slimes))
# ????

# profit!
