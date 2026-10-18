"""Experiment 7: Quick Sort and Merge Sort with execution-time comparison."""
import random
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def quick_sort(values):
    """Return a sorted copy using Quick Sort (recursive, last element pivot)."""
    arr = values.copy()

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    if arr:
        sort(0, len(arr) - 1)
    return arr


def merge_sort(values):
    """Return a sorted copy using Merge Sort."""
    if len(values) <= 1:
        return values.copy()
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def read_numbers():
    input_file = BASE_DIR / "input.txt"
    if input_file.exists():
        content = input_file.read_text(encoding="utf-8").strip()
        if content:
            try:
                return [int(item) for item in content.replace(",", " ").split()]
            except ValueError:
                print("Warning: input.txt contains invalid data; using built-in sample.")
    return [38, 27, 43, 3, 9, 82, 10, 15, 1, 55]


def main():
    numbers = read_numbers()
    print("Original array:")
    print(*numbers)

    start = time.perf_counter()
    quick_result = quick_sort(numbers)
    quick_time = time.perf_counter() - start

    start = time.perf_counter()
    merge_result = merge_sort(numbers)
    merge_time = time.perf_counter() - start

    print("\nQuick Sort result:")
    print(*quick_result)
    print(f"Quick Sort execution time: {quick_time:.8f} seconds")

    print("\nMerge Sort result:")
    print(*merge_result)
    print(f"Merge Sort execution time: {merge_time:.8f} seconds")

    print("\nCorrectness check:", "PASS" if quick_result == merge_result == sorted(numbers) else "FAIL")
    output = (
        "Experiment 7: Quick Sort and Merge Sort\n"
        f"Original array: {' '.join(map(str, numbers))}\n"
        f"Quick Sort result: {' '.join(map(str, quick_result))}\n"
        f"Quick Sort execution time: {quick_time:.8f} seconds\n"
        f"Merge Sort result: {' '.join(map(str, merge_result))}\n"
        f"Merge Sort execution time: {merge_time:.8f} seconds\n"
        f"Correctness check: {'PASS' if quick_result == merge_result == sorted(numbers) else 'FAIL'}\n"
    )
    (BASE_DIR / "output.txt").write_text(output, encoding="utf-8")
    print("\nResults saved to output.txt")


if __name__ == "__main__":
    main()
