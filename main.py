class TreeNode:
    """
    Binary tree node for Wi-Fi routers.

    value: integer capacity
    left, right: TreeNode or None
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_level_sum(root):
    
    if root is None:
        return (None, 0)

    from collections import deque
    queue = deque([root])
    level = 0
    best_level = 0
    best_sum = root.value

    while queue:
        level_sum = 0
        nodes_in_level = len(queue)
        for _ in range(nodes_in_level):
            node = queue.popleft()
            level_sum += node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if level_sum > best_sum or (level_sum == best_sum and level < best_level):
            best_sum = level_sum
            best_level = level
        level += 1
    return (best_level, best_sum)


if __name__ == "__main__":
    
    left = TreeNode(5, TreeNode(4), TreeNode(1))
    right = TreeNode(7)
    root = TreeNode(10, left, right)
    print(max_level_sum(root))
