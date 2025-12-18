# Using slicing
arr=[1,2,3,4]
print("Reversed array:", arr[::-1])

# Using reverse() method
arr.reverse()
print("Reversed array using reverse():", arr)

# Using loop
def reverse_array(arr):
    start, end = 0, len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

print("Reversed using function:", reverse_array([1,2,3,4,5]))
