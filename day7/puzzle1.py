import sys

curr_dir = None
directories = {}


def get_path(path, dir):
    if path == "/":
        return path + dir
    else:
        return path + "/" + dir


def calc_total(path, lines):
    directories[path] = 0

    while len(lines) > 0:
        line = lines.pop(0).strip()
        if line.startswith("$ "):
            # process command
            if line[2:].startswith("cd"):
                new_dir = line[2:].split(" ")[1]
                if new_dir == "..":
                    return directories[path]
                else:
                    total = calc_total(get_path(path, new_dir), lines)
                    directories[path] += total
            else:
                # ignore ls for now
                pass
        elif line.startswith("dir "):
            # ignore dirs for now
            pass
        else:
            # file, add the total to curr dir
            directories[path] += int(line.split(" ")[0])

    return directories[path]


sys.setrecursionlimit(1500)

with open("./input.txt") as fp:
    lines = fp.readlines()
    line = lines.pop(0).strip()

    if line.startswith("$ cd "):
        calc_total(line[2:].split(" ")[1], lines)
    else:
        print("Didn't start at the root")
        exit(1)

print(sum(filter(lambda t: t <= 100_000, directories.values())))
