def sum_nodes(root):
    if not root:
        return 0
    return root.data + sum_nodes(root.left) + sum_nodes(root.right)
