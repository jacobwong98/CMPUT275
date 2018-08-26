# read the first line
num_sec, num_res = tuple(int(i) for i in input().split())
array = []
array.append(0)

callpersec = list(int(i) for i in input().split())
# read and process each query
for i in range(1, num_sec+1):
    array.append(array[i-1] + callpersec[i-1])

for _ in range(num_res):
    start, end = tuple(int(i) for i in input().split())
    print(array[end] - array[start-1])
