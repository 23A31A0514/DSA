# Creating an array
arr = [1, 2, 3, 4, 5]
print("Array:", arr)

# Access elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Update element
arr[2] = 10
print("Updated array:", arr)

# Append element
arr.append(6)
print("After append:", arr)

# Insert element at index
arr.insert(1, 15)
print("After insert:", arr)

# Delete element by index
arr.pop(3)  # removes element at index 3
print("After pop:", arr)

# Delete element by value
arr.remove(15)
print("After remove:", arr)

# Length of array
print("Length:", len(arr))
