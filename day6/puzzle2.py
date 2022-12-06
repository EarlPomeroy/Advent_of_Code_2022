
from collections import Counter


def is_unique(test):
    wc = Counter(test)

    # Finding no. of  occurrence of a character
    # and get the index of it.
    for _, count in wc.items():
        if (count > 1):
            return False

    return True


found = False

with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        # process all just in case
        for n in range(0, len(line)-13):
            test = line[n:n+14]
            if is_unique(test):
                print(f'Start-of-packet found {test} at {n+14}')
                found = True
                break

if not found:
    print("no start-of-packet found")
