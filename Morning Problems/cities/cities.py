n = int(input())
path = {}

for i in range(n):
    start, end = input().split("---")
    # now we have the two strings for each of the first n lines
    # do something with them!
    path[start] = end

# you still have to read in the 2nd part of the input
# which consists of the value q followed by the q query lines
m = int(input())

for j in range(m):
    citiesStart = input()
    counter = 0
    while citiesStart != "Edmonton":
        citiesStart = path[citiesStart]
        counter += 1
    print(counter)
