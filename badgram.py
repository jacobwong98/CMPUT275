import sys
listGoodBad = []

for line in sys.stdin:
    # be mindful that line may have a trailing \n character
    if line is not '\n':
        count = 0
        temp = []
        for i in line.lower():
            if i in "vkjxqz" and i not in temp:
                count += 1
                temp.append(i)

        if count >= 5:
            listGoodBad.append("BAD")
        else:
            listGoodBad.append("OK")

for num in range(len(listGoodBad)):
    print(listGoodBad[num])
