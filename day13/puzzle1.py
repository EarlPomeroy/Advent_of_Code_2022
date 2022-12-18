import ast

correctly_ordered_indices = []
pair_list = []

# Rules:
# if left is smaller than right, correct order
# if right is smaller than left, incorrect order
# left runs out of items first, correct order
# right runs out of items first, incorrect order


def evaluate(left, right):
    """Compare two array and return the result

    Args:
        left list(any): left array
        right list(any): right array

    Returns:
        bool | None: True if the left array is sorted higher, False if the right array is sorted higher, None if the arrays are equal
    """
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

print(correctly_ordered_indices)
print(sum(correctly_ordered_indices))
