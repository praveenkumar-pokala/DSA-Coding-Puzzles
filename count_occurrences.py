# Function to find the first occurrence of a number using binary search
def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid  # Record the index and continue to search on the left
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

# Function to find the last occurrence of a number using binary search
def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid  # Record the index and continue to search on the right
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

# Function to count the number of occurrences of a target
def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:  # If the number is not present
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1

# Example usage
arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8]
target = 5

first = first_occurrence(arr, target)
last = last_occurrence(arr, target)
count = count_occurrences(arr, target)

print(f"First occurrence of {target}: {first}")
print(f"Last occurrence of {target}: {last}")
print(f"Count of {target}: {count}")
