def is_same(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.data == t2.data and
            is_same(t1.left, t2.left) and
            is_same(t1.right, t2.right))
