x_reg = []


def process(instruction, value):
    last_val = 1

    if len(x_reg) > 0:
        last_val = x_reg[-1]

    if instruction == "addx":
        x_reg.append(last_val)
        x_reg.append(last_val + int(value))
    else:
        x_reg.append(last_val)


def calculate_signal_strength():
    include = False
    strength = 0

    for i in range(0, len(x_reg), 20):
        if include:
            strength += i * x_reg[i-2]

        include = not include

    return strength


with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        instruction = line.strip()
        value = None

        if instruction.startswith("addx"):
            instruction, value = instruction.split()

        process(instruction, value)

print(calculate_signal_strength())
