"""Experiment 1: AVL Tree implementation with file handling.

Reads initial integer values from input.txt when the file exists; otherwise,
asks the user to enter them. Then performs one insertion and one deletion,
prints the final inorder traversal, and writes it to output.txt.
"""

from pathlib import Path


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    return node.height if node else 0


def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))


def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0


def right_rotate(y):
    x = y.left
    subtree = x.right
    x.right = y
    y.left = subtree
    update_height(y)
    update_height(x)
    return x


def left_rotate(x):
    y = x.right
    subtree = y.left
    y.left = x
    x.right = subtree
    update_height(x)
    update_height(y)
    return y


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # Ignore duplicate keys.

    update_height(root)
    balance = balance_factor(root)

    # Left-left case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    # Right-right case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    # Left-right case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right-left case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def minimum_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = minimum_node(root.right)
        root.key = successor.key
        root.right = delete(root.right, successor.key)

    update_height(root)
    balance = balance_factor(root)

    # Left-heavy tree
    if balance > 1 and balance_factor(root.left) >= 0:
        return right_rotate(root)
    if balance > 1 and balance_factor(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right-heavy tree
    if balance < -1 and balance_factor(root.right) <= 0:
        return left_rotate(root)
    if balance < -1 and balance_factor(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.key)
        inorder(root.right, result)
    return result


def read_initial_values():
    input_path = Path(__file__).with_name("input.txt")
    if input_path.exists():
        contents = input_path.read_text(encoding="utf-8").strip()
        if contents:
            try:
                values = [int(item) for item in contents.split()]
                print(f"Initial values read from {input_path.name}: {values}")
                return values
            except ValueError as exc:
                raise ValueError("input.txt must contain integers separated by spaces or new lines.") from exc

    raw = input("Enter initial elements separated by spaces: ").strip()
    if not raw:
        return []
    try:
        return [int(item) for item in raw.split()]
    except ValueError as exc:
        raise ValueError("Please enter integers separated by spaces.") from exc


def main():
    try:
        values = read_initial_values()
        root = None
        for value in values:
            root = insert(root, value)

        print("Initial inorder traversal:", *inorder(root))

        insert_raw = input("Enter an element to insert: ").strip()
        if insert_raw:
            root = insert(root, int(insert_raw))

        delete_raw = input("Enter an element to delete: ").strip()
        if delete_raw:
            root = delete(root, int(delete_raw))

        final_values = inorder(root)
        output_text = "Final inorder traversal: " + " ".join(map(str, final_values))
        print(output_text)

        output_path = Path(__file__).with_name("output.txt")
        output_path.write_text(output_text + "\n", encoding="utf-8")
        print(f"Output saved to {output_path.name}")
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
