# read the input
enterString = input()
lengthString = len(enterString)
counter = 0
lengthMax = 1
low = 0
high = 0

for i in range(1, lengthString):
    low = i - 1
    high = i + 1
    while low >= 0 and high < lengthString and enterString[low] == enterString[high]:
        if high - low + 1 > lengthMax:
            counter = low
            lengthMax = high - low + 1
        low -= 1
        high += 1
print(lengthMax)
# print the answer!
