"""Experiment 3: Implementation of Max Heap and Min Heap using Python."""

import heapq
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"


def read_numbers():
    """Read initial integers from input.txt, or ask the user if it is empty."""
    try:
        contents = INPUT_FILE.read_text(encoding="utf-8").strip()
        if contents:
            return [int(value) for value in contents.replace(",", " ").split()]
    except FileNotFoundError:
        pass

    raw = input("Enter initial integers separated by spaces: ").strip()
    return [int(value) for value in raw.replace(",", " ").split()] if raw else []


def show_heap(heap, is_max_heap):
    """Display heap in its internal array representation."""
    if is_max_heap:
        return [-value for value in heap]
    return list(heap)


def main():
    numbers = read_numbers()
    max_heap = [-value for value in numbers]
    min_heap = list(numbers)
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    print("\nInitial elements:", numbers)
    print("Max Heap:", show_heap(max_heap, True))
    print("Min Heap:", show_heap(min_heap, False))

    while True:
        print("\n--- Heap Operations ---")
        print("1. Insert into Max Heap")
        print("2. Delete maximum from Max Heap")
        print("3. Insert into Min Heap")
        print("4. Delete minimum from Min Heap")
        print("5. Display both heaps")
        print("6. Heap sort (ascending)")
        print("0. Exit and save output")

        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                value = int(input("Enter value: "))
                heapq.heappush(max_heap, -value)
                print("Max Heap:", show_heap(max_heap, True))
            elif choice == "2":
                if max_heap:
                    print("Deleted maximum:", -heapq.heappop(max_heap))
                else:
                    print("Max Heap is empty.")
            elif choice == "3":
                value = int(input("Enter value: "))
                heapq.heappush(min_heap, value)
                print("Min Heap:", show_heap(min_heap, False))
            elif choice == "4":
                if min_heap:
                    print("Deleted minimum:", heapq.heappop(min_heap))
                else:
                    print("Min Heap is empty.")
            elif choice == "5":
                print("Max Heap:", show_heap(max_heap, True))
                print("Min Heap:", show_heap(min_heap, False))
            elif choice == "6":
                print("Sorted elements (ascending):", sorted(numbers))
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid integer.")

    final_max = show_heap(max_heap, True)
    final_min = show_heap(min_heap, False)
    output = (
        "Final Max Heap: " + str(final_max) + "\n" +
        "Final Min Heap: " + str(final_min) + "\n"
    )
    OUTPUT_FILE.write_text(output, encoding="utf-8")
    print("\n" + output, end="")
    print("Results saved to output.txt")


if __name__ == "__main__":
    main()
