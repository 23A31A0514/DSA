def delete(key):
    index = hash_function(key)
    if hash_table[index] == key:
        hash_table[index] = None
