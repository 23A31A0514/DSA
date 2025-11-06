arr = [1, 2, 3, 4, 5]

# Left rotation by 2
def left_rotate(arr, d):
    return arr[d:] + arr[:d]

# Right rotation by 2
def right_rotate(arr, d):
    return arr[-d:] + arr[:-d]

print("Left rotate by 2:", left_rotate(arr, 2))
print("Right rotate by 2:", right_rotate(arr, 2))
