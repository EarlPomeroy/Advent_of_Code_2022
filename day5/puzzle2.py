from queue import LifoQueue

temp_stack = LifoQueue()
stacks = []
create_stacks = False
found_cmd_start = False


def process_stacks():
    # get the numbers line and discard it.
    temp_stack.get()
    temp_stack.get()

    while not temp_stack.empty():
        line = temp_stack.get()
        index = 0
        while len(line) > 0:
            container = line[:4].strip()
            if len(container) > 0:
                stacks[index].put(container.strip('[').strip(']'))
            index += 1
            line = line[4:]


with open("./input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        if not create_stacks:
            stacks = [None] * int(len(line)/4)

            for idx, _ in enumerate(stacks):
                stacks[idx] = LifoQueue()

            create_stacks = True

        if not found_cmd_start:
            temp_stack.put(line)

        if len(line.strip()) == 0:
            found_cmd_start = True
            process_stacks()
            continue

        if found_cmd_start:
            _, count, _, from_queue, _, to_queue = line.strip().split()

            temp_stack = LifoQueue()
            i = 0
            while i < int(count):
                container = stacks[int(from_queue) - 1].get()
                temp_stack.put(container)
                i += 1

            while not temp_stack.empty():
                stacks[int(to_queue) - 1].put(temp_stack.get())


result = ""

for n in stacks:
    result += n.get()

print(result)
