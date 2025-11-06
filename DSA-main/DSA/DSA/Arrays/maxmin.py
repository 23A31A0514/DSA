arr = [3, 7, 1, 9, 2]

print("Maximum:", max(arr))
print("Minimum:", min(arr))

# Without built-in functions
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

print("Maximum using loop:", find_max(arr))
