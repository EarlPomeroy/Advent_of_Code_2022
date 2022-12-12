class Monkey:
    def __init__(self, id, items, operation, test, true_monkey, false_monkey) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0
        self.op = None
        self.val = None
        self.both_old = False

    def inspect(self):
        true_list = []
        false_list = []

        while len(self.items) > 0:
            self.inspections += 1
            item = self.items.pop(0)
            new = self.eval(item)
            if self.perform_test(new):
                true_list.append(new)
            else:
                false_list.append(new)

        return {self.true_monkey: true_list, self.false_monkey: false_list}

    def eval(self, item):
        if self.op == None:
            val1, operator, val2 = self.operation.split()
            self.op = operator
            if val1 == "old" and val2 == "old":
                self.both_old = True
            elif val1 == "old":
                self.val = int(val2)
            else:
                self.val = int(val1)

        if self.both_old:
            self.val = item

        if self.op == "+":
            return int((item + self.val) / 3)
        else:
            return int((item * self.val) / 3)

    def perform_test(self, item):
        return item % self.test == 0


monkeys = []

with open("./input.txt") as fp:
    lines = fp.readlines()
    id = None
    items = None
    operation = None
    test = None
    true_monkey = None
    false_monkey = None

    for i, line in enumerate(lines, start=1):
        line = line.strip()
        match i % 7:
            case 1:
                id = int(line.split()[1].removesuffix(":"))
            case 2:
                items = list(map(int, line.split(":")[1].strip().split(",")))
            case 3:
                operation = line.split("=")[1].strip()
            case 4:
                test = int(line[line.rfind(" "):])
            case 5:
                true_monkey = int(line[line.rfind(" "):])
            case 6:
                false_monkey = int(line[line.rfind(" "):])
            case _:
                monkeys.append(Monkey(id, items, operation,
                               test, true_monkey, false_monkey))

    # add the last monkey since there was no seventh line in the input
    monkeys.append(Monkey(id, items, operation,
                   test, true_monkey, false_monkey))

for round in range(0, 20):
    for m in monkeys:
        monkey_business = m.inspect()

        for key, value in monkey_business.items():
            monkeys[key].items.extend(value)

top_banana = -1
second_banana = -1

for m in monkeys:
    if m.inspections > top_banana:
        second_banana = top_banana
        top_banana = m.inspections
    elif m.inspections > second_banana:
        second_banana = m.inspections

print(top_banana * second_banana)
