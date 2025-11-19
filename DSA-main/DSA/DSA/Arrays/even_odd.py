arr = [1, 2, 3, 4, 5, 6]
even = sum(1 for x in arr if x % 2 == 0)
odd = len(arr) - even
print("Even:", even, "Odd:", odd)
