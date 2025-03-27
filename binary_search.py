# Binary Search Implementation in Python

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the target is not found

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")