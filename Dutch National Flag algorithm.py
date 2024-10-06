def dutch_flag_partition(arr, pivot_index):
    pivot = arr[pivot_index]
    smaller = 0  # Pointer for the next position of the smaller element
    equal = 0    # Pointer for the current element
    larger = len(arr) - 1  # Pointer for the next position of the larger element

    while equal <= larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:  # arr[equal] > pivot
            arr[equal], arr[larger] = arr[larger], arr[equal]
            larger -= 1

    return arr

# Example usage
if __name__ == "__main__":
    arr = [3, 2, 1, 2, 3, 1, 2]
    pivot_index = 1  # We can choose any index; here, we use the second element as pivot
    sorted_arr = dutch_flag_partition(arr, pivot_index)
    print("Sorted array:", sorted_arr)
