"""B-tree of order 5 (maximum 5 children / 4 keys per node)."""

from dataclasses import dataclass, field
from typing import List, Optional

ORDER = 5
MAX_KEYS = ORDER - 1


@dataclass
class BTreeNode:
    keys: List[int] = field(default_factory=list)
    children: List["BTreeNode"] = field(default_factory=list)

    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0


class BTree:
    def __init__(self) -> None:
        self.root = BTreeNode()

    def insert(self, key: int) -> None:
        promoted = self._insert_recursive(self.root, key)
        if promoted is not None:
            middle_key, right_node = promoted
            old_root = self.root
            self.root = BTreeNode(keys=[middle_key], children=[old_root, right_node])

    def _insert_recursive(self, node: BTreeNode, key: int):
        """Insert key; return (promoted_key, right_node) when node splits."""
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return None  # Ignore duplicate keys.

        if node.is_leaf:
            node.keys.insert(i, key)
        else:
            result = self._insert_recursive(node.children[i], key)
            if result is not None:
                promoted_key, right_child = result
                node.keys.insert(i, promoted_key)
                node.children.insert(i + 1, right_child)

        if len(node.keys) <= MAX_KEYS:
            return None

        # A 5-key overflow is split around its middle key.
        middle = len(node.keys) // 2
        promoted_key = node.keys[middle]
        right_node = BTreeNode(
            keys=node.keys[middle + 1 :],
            children=node.children[middle + 1 :] if node.children else [],
        )
        node.keys = node.keys[:middle]
        if node.children:
            node.children = node.children[: middle + 1]
        return promoted_key, right_node

    def search(self, key: int) -> bool:
        node = self.root
        while True:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and node.keys[i] == key:
                return True
            if node.is_leaf:
                return False
            node = node.children[i]

    def inorder(self) -> List[int]:
        result: List[int] = []

        def visit(node: BTreeNode) -> None:
            for i, key in enumerate(node.keys):
                if node.children:
                    visit(node.children[i])
                result.append(key)
            if node.children:
                visit(node.children[-1])

        visit(self.root)
        return result

    def display_levels(self) -> None:
        queue = [self.root]
        level = 0
        while queue:
            next_level = []
            parts = []
            for node in queue:
                parts.append("[" + " ".join(map(str, node.keys)) + "]")
                next_level.extend(node.children)
            print(f"Level {level}: " + "  ".join(parts))
            queue = next_level
            level += 1


def read_input(filename: str = "input.txt") -> List[int]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read().strip()
        return [int(value) for value in contents.split()] if contents else []
    except FileNotFoundError:
        return []
    except ValueError:
        print("Warning: input.txt should contain integers separated by spaces.")
        return []


def main() -> None:
    values = read_input()
    if not values:
        raw = input("Enter integers to insert, separated by spaces: ").strip()
        try:
            values = [int(value) for value in raw.split()]
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return

    tree = BTree()
    for value in values:
        tree.insert(value)

    print("B-tree of order 5")
    print("Inserted keys:", " ".join(map(str, values)))
    print("Tree structure:")
    tree.display_levels()
    print("Inorder traversal:", " ".join(map(str, tree.inorder())))

    raw_search = input("Enter a key to search: ").strip()
    try:
        search_key = int(raw_search)
    except ValueError:
        print("Invalid search key. Please enter an integer.")
        return

    if tree.search(search_key):
        print(f"Key {search_key} found in the B-tree.")
    else:
        print(f"Key {search_key} not found in the B-tree.")

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("B-tree of order 5\n")
        file.write("Inorder traversal: " + " ".join(map(str, tree.inorder())) + "\n")
    print("Traversal saved to output.txt")


if __name__ == "__main__":
    main()
