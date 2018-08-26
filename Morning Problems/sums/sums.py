# read the Inputs
sizeList = int(input())
list1 = [int(i) for i in input().split()]
list2 = set([int(i) for i in input().split()])
list3 = [int(i) for i in input().split()]
counter = 0


for i in list3:
    for j in list1:
        if i-j in list2:
            counter += 1
            break

print(counter)
# solve the problem

# print the answer

# be mindful of the running time: O(n^3) is not fast enough
