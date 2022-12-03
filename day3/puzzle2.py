from itertools import islice

score = 0


def get_score(val):
    if val in range(ord('A'), ord('Z') + 1):
        return val - 38
    else:
        return val - 96


with open("./input.txt") as fp:

    while True:
        next_n_lines = list(islice(fp, 3))
        if not next_n_lines:
            break
        first = next_n_lines[0].strip()
        second = next_n_lines[1].strip()
        third = next_n_lines[2].strip()

        match = None
        for c in first:
            if c in second and c in third:
                match = ord(c)
                break

        score += get_score(match)

print(score)
