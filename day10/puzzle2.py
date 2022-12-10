screen = [["."] * 40, ["."] * 40, ["."] *
          40, ["."] * 40, ["."] * 40, ["."] * 40]
cycle = 0
x_reg = []


def get_last_x_reg():
    last_val = 1

    if len(x_reg) > 0:
        last_val = x_reg[-1]

    return last_val


def process(instruction, value):
    last_val = get_last_x_reg()

    if instruction == "addx":
        draw_pixel(get_last_x_reg())
        x_reg.append(last_val)
        draw_pixel(get_last_x_reg())
        x_reg.append(last_val + int(value))
    else:
        draw_pixel(get_last_x_reg())
        x_reg.append(last_val)


def draw_pixel(x_val):
    global cycle

    col = cycle % 40

    if x_val - 2 < col < x_val + 2:
        row = int(cycle/40)
        screen[row][col] = "#"

    cycle += 1


def calculate_signal_strength():
    include = False
    strength = 0

    for i in range(0, len(x_reg), 20):
        if include:
            print(i, x_reg[i-2])
            strength += i * x_reg[i-2]

        include = not include

    return strength


def print_screen():
    output = ""
    for line in screen:
        output += "".join(line) + "\n"

    print(output)


with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        instruction = line.strip()
        value = None

        if instruction.startswith("addx"):
            instruction, value = instruction.split()

        process(instruction, value)

print_screen()
