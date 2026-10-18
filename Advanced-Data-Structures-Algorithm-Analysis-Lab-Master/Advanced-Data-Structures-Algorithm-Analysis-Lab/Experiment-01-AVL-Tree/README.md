# Experiment 1: AVL Tree Using Python

## Aim
To implement an AVL tree with insertion, deletion, balancing rotations, and inorder traversal. Initial values are read from a text file when available, and the final traversal is written to an output file.

## Requirements
- Python 3
- No external libraries required

## Files
- `avl_tree.py` — complete Python implementation
- `input.txt` — initial values, separated by spaces or new lines
- `sample_output.txt` — example console output
- `output.txt` — generated automatically when the program runs

## How to Run
1. Keep `avl_tree.py` and `input.txt` in the same folder.
2. Run:
   ```bash
   python avl_tree.py
   ```
3. Enter an element to insert and an element to delete when prompted.
4. The final inorder traversal appears in the terminal and is saved to `output.txt`.

If `input.txt` is missing or empty, the program asks for initial values interactively.

## Sample Test
`input.txt`:
```text
30 20 40 10 25
```
Example responses:
```text
35
20
```
Expected final inorder traversal:
```text
10 25 30 35 40
```

## Concepts Covered
- AVL tree and balance factor
- LL, RR, LR, and RL rotations
- Insertion and deletion with rebalancing
- Inorder traversal
- Basic input/output file handling

## Result
The AVL tree operations were implemented successfully in Python.
