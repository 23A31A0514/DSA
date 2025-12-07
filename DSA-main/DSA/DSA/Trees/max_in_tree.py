def find_max(root):
    if not root:
        return float('-inf')
    return max(root.data, find_max(root.left), find_max(root.right))
