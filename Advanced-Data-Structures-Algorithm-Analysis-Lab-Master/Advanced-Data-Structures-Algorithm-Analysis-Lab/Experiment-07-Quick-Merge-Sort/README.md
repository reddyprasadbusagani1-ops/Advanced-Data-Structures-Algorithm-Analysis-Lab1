# Experiment 7: Quick Sort and Merge Sort

## Aim
To implement Quick Sort and Merge Sort in Python, measure their execution times, and compare their sorted results.

## Language
Python 3 (no external libraries required)

## Files
- `sorting_analysis.py` — implementation of both sorting algorithms and execution-time comparison
- `input.txt` — sample list of integers
- `sample_output.txt` — sample run (timings vary by device)
- `output.txt` — generated results after running the program

## How to Run
1. Install Python 3.
2. Keep `sorting_analysis.py` and `input.txt` in the same folder.
3. Run in a terminal:
   ```bash
   python sorting_analysis.py
   ```
4. The sorted arrays and measured execution times are printed and saved to `output.txt`.

## Algorithms
- **Quick Sort:** partitions the array around a pivot and recursively sorts the partitions. Average time complexity: `O(n log n)`; worst case: `O(n²)`.
- **Merge Sort:** divides the array, sorts each half, and merges the results. Time complexity: `O(n log n)`.

## Result
Quick Sort and Merge Sort were implemented successfully. Both algorithms produce the same sorted result; execution times depend on the input and device.
