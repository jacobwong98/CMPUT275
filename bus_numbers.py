n = int(input())
bus_numbers = [int(i) for i in input().split()]
bus_numbers = sorted(bus_numbers)

sequences = []
sequences.append([bus_numbers[0]])
for i in range(1, len(bus_numbers)):
    if bus_numbers[i]-bus_numbers[i-1] == 1:
        sequences[-1].append(bus_numbers[i])
    else:
        sequences.append([bus_numbers[i]])
result = ' '
for i in sequences:
    if len(i) <= 2:
        result += ' '.join(str(x) for x in i)
    else:
        result += '{}-{}'.format(i[0], i[-1])
    result += ' '

print(result[:len(result)-1])
