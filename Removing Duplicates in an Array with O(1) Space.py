def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Initialize a pointer for the position of the next unique element
    unique_index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]
    
    # Return the length of the array with unique elements
    return unique_index + 1

# Example usage
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 4, 5]
    length = remove_duplicates(nums)
    print("Array after removing duplicates:", nums[:length])
    print("Length of array with unique elements:", length)
