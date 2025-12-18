# Linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

print("\nIndex of 10:", linear_search([1,2,3,4], 10))
