elf_calories = []

with open("./input.txt") as fp:
	curr_elf = 0
	lines = fp.readlines()
	for line in lines:
		if len(line.strip()) > 0:
			curr_elf += int(line)
		else:
			elf_calories.append(curr_elf)
			curr_elf = 0

elf_calories.sort(reverse=True)

print(elf_calories[0] + elf_calories[1]+ elf_calories[2])