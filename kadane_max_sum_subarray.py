def kadane_max_sum_subarray(arr):
    max_sum = float('-inf')  # Initialize maximum sum to negative infinity
    current_sum = 0           # Initialize current sum to 0
    start = 0                 # Start index of the maximum sum subarray
    end = 0                   # End index of the maximum sum subarray
    temp_start = 0            # Temporary start index for the current subarray

    for i in range(len(arr)):  # Loop through each element in the array
        current_sum += arr[i]  # Add the current element to current_sum

        if current_sum > max_sum:  # Check if current_sum is greater than max_sum
            max_sum = current_sum   # Update max_sum
            start = temp_start      # Update the start index of the max subarray
            end = i                 # Update the end index to current position

        if current_sum < 0:         # If current_sum is negative
            current_sum = 0         # Reset current_sum to 0
            temp_start = i + 1      # Update temp_start to the next index

    return max_sum, arr[start:end + 1]  # Return the maximum sum and the corresponding subarray


# Example usage
example_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = kadane_max_sum_subarray(example_array)

print("Maximum sum:", max_sum)  # Output: Maximum sum: 6
print("Subarray:", subarray)     # Output: Subarray: [4, -1, 2, 1]
