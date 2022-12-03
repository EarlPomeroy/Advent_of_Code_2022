score = 0


def get_score(val):
    if val in range(ord('A'), ord('Z') + 1):
        return val - 38
    else:
        return val - 96


with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        ruck = line.strip()

        midpoint = int(len(ruck)/2)
        comp1 = ruck[:midpoint]
        comp2 = ruck[midpoint:]

        match = None
        for c in comp1:

            if c in comp2:
                match = ord(c)
                break

        score += get_score(match)

print(score)
