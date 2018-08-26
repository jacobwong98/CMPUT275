# a queue may be helpful, but is not necessary
from collections import deque
# read the Inputs
n, q = list(map(int, input().rstrip('\r\n').split()))
deq = deque(range(n))
# solve the problem
i = 0
while len(deq) > 1:
    temp = deq.popleft()
    if i % q == 0 and i != 0:
        i = 1
    else:
        deq.append(temp)
        i += 1
# print the answer
print(deq.pop())
# Be mindful of running time, deleting an item in the middle of a list is
# too expensive! The intended running time is O(n*q).

# If the test center is taking forever, press ctrl-c from the terminal
# where you launched the test center to quit it prematurely.
