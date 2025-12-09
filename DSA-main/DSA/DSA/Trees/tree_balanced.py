def check_balance(root):
    if not root:
        return 0
    lh = check_balance(root.left)
    rh = check_balance(root.right)

    if abs(lh - rh) > 1:
        return -1
    if lh == -1 or rh == -1:
        return -1

    return 1 + max(lh, rh)
