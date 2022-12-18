import ast

ordered_signal_list = []

# Rules:
# if left is smaller than right, correct order
# if right is smaller than left, incorrect order
# left runs out of items first, correct order
# right runs out of items first, incorrect order


def evaluate(left: list, right: list) -> bool | None:
    """Compare two array and return the result

    Args:
        left (list): left array
        right (list): right array

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


def merge_sort(arr: list) -> None:
    """Perform an in-play merge sort an array

    Args:
        arr (list): list to sort
    """
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


with open("./test.txt") as fp:
    use_left = True
    left = None
    right = None
    lines = fp.readlines()
    for line in list(map(str.strip, lines)):
        if len(line) > 0:
            ordered_signal_list.append(ast.literal_eval(line.strip()))

# append the delimiters
ordered_signal_list.append([[2]])
ordered_signal_list.append([[6]])

merge_sort(ordered_signal_list)

i = ordered_signal_list.index([[2]])
j = ordered_signal_list.index([[6]])

print((i + 1) * (j + 1))
