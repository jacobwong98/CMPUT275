words = input().split()

# words is now a list of all strings in the input

dictionary = {}
result = []

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1


for key in dictionary:
    if dictionary[key] == max(dictionary.values()):
        result.append(key)

result.sort()
print('\n'.join(result))
# finish the problem!
