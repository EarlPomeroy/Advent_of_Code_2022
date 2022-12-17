import ast

correctly_ordered_indices = []
pair_list = []
ordered_signal_list = []


# Rules:
# if left is smaller than right, correct order
# if right is smaller than left, incorrect order
# left runs out of items first, correct order
# right runs out of items first, incorrect order


def evaluate(left, right):
    l_len = len(left)
    r_len = len(right)
    add_index = None

    for i in range(0, max(l_len, r_len)):
        if i >= l_len:
            add_index = True
            break
        elif i >= r_len:
            add_index = False
            break
        else:
            l_val = left[i]
            r_val = right[i]
            if type(l_val) is int and type(r_val) is int:
                if l_val < r_val:
                    add_index = True
                    break
                elif l_val > r_val:
                    add_index = False
                    break
                else:
                    continue
            elif type(l_val) is list and type(r_val) is list:
                result = evaluate(l_val, r_val)
                if result is not None:
                    add_index = result
                    break
            elif type(l_val) is int and type(r_val) is list:
                result = evaluate([l_val], r_val)
                if result is not None:
                    add_index = result
                    break
            elif type(l_val) is list and type(r_val) is int:
                result = evaluate(l_val, [r_val])
                if result is not None:
                    add_index = result
                    break

    return add_index


def merge_sort(arr):
    if len(arr) > 1:
        midpoint = int(len(arr)/2)

        left = arr[:midpoint]
        merge_sort(left)

        right = arr[midpoint:]
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if evaluate(left[i], right[j]) == False:
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


with open("./input.txt") as fp:
    use_left = True
    left = None
    right = None
    lines = fp.readlines()
    for line in list(map(str.strip, lines)):
        if len(line) > 0:
            if use_left:
                left = ast.literal_eval(line.strip())
                use_left = not use_left
            else:
                right = ast.literal_eval(line.strip())
                use_left = not use_left
        else:
            pair_list.append((left, right))
            left = None
            right = None
            use_left = True

    # Add the last line since there was no blank line after to complete the processing
    pair_list.append((left, right))

index = 1

for pair in pair_list:
    if evaluate(pair[0], pair[1]):
        correctly_ordered_indices.append(index)
    index += 1

# Move the valid pair into an array for sorting, note: off by one
for i in range(0, len(pair_list)):
    left, right = pair_list[i]
    ordered_signal_list.append(left)
    ordered_signal_list.append(right)

# append the delimiters
ordered_signal_list.append([[2]])
ordered_signal_list.append([[6]])

merge_sort(ordered_signal_list)

i = ordered_signal_list.index([[2]])
j = ordered_signal_list.index([[6]])

print((i + 1) * (j + 1))
