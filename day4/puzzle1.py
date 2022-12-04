contained = 0

with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        range1, range2 = line.strip().split(",")
        r1_min, r1_max = map(int, range1.split("-"))
        r2_min, r2_max = map(int, range2.split("-"))

        if (r1_min <= r2_min and r1_max >= r2_max) or (r2_min <= r1_min and r2_max >= r1_max):
            contained += 1

print(contained)