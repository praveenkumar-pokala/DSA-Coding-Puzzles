def longest_increasing_subsequence(arr):
    n = len(arr)
    
    # Array to store the length of the longest increasing subsequence ending at each index
    lis = [1] * n
    
    # Array to store the previous index of the element that is part of the LIS
    prev = [-1] * n
    
    # Calculate lis values for each index
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prev[i] = j  # Track the index of the previous element in the LIS
    
    # The length of the longest increasing subsequence is the maximum value in lis[]
    max_length = max(lis)
    
    # Find the index of the maximum value in lis[]
    max_index = lis.index(max_length)
    
    # Reconstruct the LIS by backtracking through the prev array
    result = []
    while max_index != -1:
        result.append(arr[max_index])
        max_index = prev[max_index]
    
    # Since we built the result array from the end, reverse it to get the correct sequence
    result.reverse()
    
    return max_length, result

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
length, subsequence = longest_increasing_subsequence(arr)
print("Length of LIS:", length)
print("LIS:", subsequence)
