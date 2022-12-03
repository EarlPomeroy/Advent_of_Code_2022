my_points = 0

with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        them, you = line.strip().split(" ")

        # 1 for Rock, 2 for Paper, and 3 for Scissors
        # 0 if you lost, 3 if the round was a draw, and 6 if you won

        # A = Rock, B = Paper, C = Scissors
        # X = Lose, Y = Draw, Z = Win
        match them:
            case "A":
                match you:
                    case "X":
                        my_points += 3
                    case "Y":
                        my_points += 4
                    case "Z":
                        my_points += 8
            case "B":
                match you:
                    case "X":
                        my_points += 1
                    case "Y":
                        my_points += 5
                    case "Z":
                        my_points += 9
            case "C":
                match you:
                    case "X":
                        my_points += 2
                    case "Y":
                        my_points += 6
                    case "Z":
                        my_points += 7

print(my_points)
