def binary_search(arr, min_index, max_index, x):
    if max_index >= min_index:
        i = int(min_index + (max_index - min_index) / 2)  # average
        if arr[i] == x:
            return i
        elif arr[i] < x:
            return binary_search(arr, i + 1, max_index, x)
        elif arr[i] > x:
            return binary_search(arr, min_index, i - 1, x)
    else:
        return -1


print(binary_search([1, 4, 12, 43, 100], 0, 4, 2))
