arr = [5, 2, 9, 1, 5, 6]

# Using built-in sort
arr.sort()
print("Sorted array:", arr)

# Descending order
arr.sort(reverse=True)
print("Descending:", arr)

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Bubble Sort:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
