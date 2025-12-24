def insert(key):
    index = hash_function(key)
    hash_table[index] = key
