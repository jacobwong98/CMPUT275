num_matches = int(input())

matchA = 0
matchB = 0
countA = 0
countB = 0

for i in range(num_matches):
    rounds = input().split()
    # now rounds is a list of the rounds in this match
    # example: if the line of input was "RR RP SR" then
    # rounds == ["RR", "RP", "SR"]
    # now do the rest!

    for j in rounds:
        if j[0] == 'R' and [1] == 'S':
            countA += 1
        elif j[0] == 'R' and j[1] == 'P':
            countB += 1
        elif j[0] == 'P' and j[1] == 'R':
            countA += 1
        elif j[0] == 'P' and j[1] == 'S':
            countB += 1
        elif j[0] == 'S' and j[1] == 'P':
            countA += 1
        elif j[0] == 'S' and j[1] == 'R':
            countB += 1
        else:
            continue

    if countA > countB:
        matchA += 1
    elif countB > countA:
        matchB += 1
    countA = 0
    countB = 0
# print here whoever is the overall winner of all the matches and
# how many matches the winner won

if matchA < matchB:
    print("Bob", matchB)
else:
    print("Alice", matchA)
