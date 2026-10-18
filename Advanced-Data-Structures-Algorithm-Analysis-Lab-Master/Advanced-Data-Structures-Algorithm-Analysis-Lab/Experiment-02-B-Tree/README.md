# Experiment 2: B-Tree of Order 5 Using Python

## Aim
To implement a B-tree of order 5 and perform insertion, search, and inorder traversal.

## Language
Python 3

## Files
- `b_tree.py` — complete Python implementation
- `input.txt` — sample integer values to insert
- `sample_output.txt` — sample program output
- `output.txt` — generated when the program runs

## Definition
A B-tree of order 5 can have at most 5 children and 4 keys in each node. When a node overflows during insertion, it is split and the middle key is promoted to its parent. Duplicate keys are ignored.

## How to Run
1. Install Python 3.
2. Keep `b_tree.py` and `input.txt` in the same folder.
3. Open a terminal in this folder and run:
   ```bash
   python b_tree.py
   ```
4. Enter a key when prompted to test searching.
5. The inorder traversal is saved to `output.txt`.

## Operations
- Insert keys into a B-tree
- Split overflowing nodes and promote middle keys
- Search for a key
- Display the tree level by level
- Perform inorder traversal
- Read input from a file and write traversal to a file

## Result
The B-tree of order 5 was implemented in Python with insertion, searching, and inorder traversal.
