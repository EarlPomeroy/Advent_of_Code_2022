my_points = 0

with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        them, you = line.strip().split(" ")

        # X = Rock, Y = Paper, Z = Scissors
        match you:
            case "X":
                my_points += 1
                if them == "C":
                    my_points += 6
                elif them == "A":
                    my_points += 3
            case "Y":
                my_points += 2
                if them == "A":
                    my_points += 6
                elif them == "B":
                    my_points += 3
            case "Z":
                my_points += 3
                if them == "B":
                    my_points += 6
                elif them == "C":
                    my_points += 3

print(my_points)
