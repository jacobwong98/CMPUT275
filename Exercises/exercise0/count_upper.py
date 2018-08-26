

input_text = input()
counter = 0

for num in input_text:
    # Checks each letter in the string
    if num.isupper():
        counter += 1

print(counter)
