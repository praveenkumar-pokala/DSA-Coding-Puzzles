def find_subarrays_with_target_sum(arr, target_sum):
    # Dictionary to store the cumulative sum and its index
    sum_map = {}
    
    # Initialize variables
    current_sum = 0
    result = []
    
    # Traverse the array
    for i in range(len(arr)):
        # Add the current element to the cumulative sum
        current_sum += arr[i]
        
        # If the current_sum is equal to the target_sum, we found a subarray from index 0 to i
        if current_sum == target_sum:
            result.append((0, i))
        
        # If (current_sum - target_sum) exists in the map, we found a subarray
        if (current_sum - target_sum) in sum_map:
            # All indices after the first occurrence of (current_sum - target_sum)
            # to i will form a subarray
            for start in sum_map[current_sum - target_sum]:
                result.append((start + 1, i))
        
        # Store the current_sum in the map with its index
        if current_sum in sum_map:
            sum_map[current_sum].append(i)
        else:
            sum_map[current_sum] = [i]
    
    return result


# Example usage
if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    target_sum = -10
    subarrays = find_subarrays_with_target_sum(arr, target_sum)
    
    if subarrays:
        print(f"Subarrays with target sum {target_sum} are:")
        for start, end in subarrays:
            print(f"Subarray from index {start} to {end}: {arr[start:end+1]}")
    else:
        print(f"No subarray with target sum {target_sum} found.")
