# Binary Search Algorithm in Python

This repository contains the implementation of the Binary Search algorithm in Python.

## How to use

1. Clone this repository.
2. Run the `binary_search.py` file with Python.
3. Use the `binary_search(arr, target)` function where `arr` is a sorted array and `target` is the element you're searching for.

## Example

```python
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")