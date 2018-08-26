'''
    Exercise 1: Word Frequency Counter
    Jacob Wong


    Sources:

    Range and Length in for loop:
    https://stackoverflow.com/questions/32554527/typeerror-list-indices-must-be-integers-or-slices-not-str

    Remove Punctuation code:
    https://stackoverflow.com/questions/4371231/removing-punctuation-from-python-list-items
'''
import sys
import argparse
import string

parser = argparse.ArgumentParser(
    description="Text frequency analysis.",
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument(
    "infile",
    help="file to be sorted, stdin if omitted",
    nargs="?",
    type=argparse.FileType('r'),
    default=sys.stdin
)
parser.add_argument(
    "--sort",
    default="byfreq",
    help="Frequency table sort options \nbyfreq - (default) sort by decreasing frequency. \nMatching frequency is resolved by word in \nincreasing lexicographical order. \nbyword- sort by word in increasing lexicographical order",
    nargs='?',
    choices=['byfreq', 'byword'],
    dest="sort"

)
parser.add_argument(
    "--ignore-case",
    help="ignore upper/lower case when doing all actions",
    action="store_true",
    dest="ignore_case"

)
parser.add_argument(
    "--remove-punct",
    help="remove all punctuation characters in a word, \npreserving only alphanumeric characters",
    action="store_true",
    dest="remove_punct"

)


args = parser.parse_args()

wordList = []

# Go through each line in the file
for line in args.infile:
    # Store the words into a list
    wordList += line.strip().split()

    if args.ignore_case:
        for word in range(len(wordList)):
            # Lower all letters in the word
            wordList[word] = wordList[word].lower()

    if args.remove_punct:
        wordList = [''.join(c for c in s if c not in string.punctuation) for s in wordList]
# Create a dictionary
frequency = {}
# Get the total number of words in the whole file
allWordNum = len(wordList)

for word in wordList:
    # .get will look through the dicitonary for the word and return 1 if it is there
    counter = frequency.get(word, 0)
    # add up the frequency and will automatically create new key if not made before
    frequency[word] = counter + 1
# Convert the dictionary into a list of tuples for sorting
keys = frequency.items()

if args.sort == "byword":
    keys = sorted(keys, key=lambda x: x[0])

if args.sort == "byfreq":
    keys = sorted(keys, key=lambda x: x[1], reverse=True)

count = 0
for key in keys:
    # Use 2 square brackets because first [] accesses the tuple number and other
    # access certain index in the tuple
    frequencyNum = keys[count][1]
    ratio = round(frequencyNum / allWordNum, 2)
    # key[] represents the tuple select by for loop so only one []
    print(key[0], frequencyNum, ratio)
    count += 1
