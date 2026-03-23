def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return index if found
    return -1  # not found


# Example usage
arr = [4, 2, 7, 1, 9]
target = 7

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")