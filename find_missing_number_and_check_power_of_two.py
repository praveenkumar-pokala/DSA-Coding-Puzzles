def find_missing_number_and_check_power_of_two(nums, n):
    """
    Finds the missing number in the array and checks if it is a power of two.

    Parameters:
    nums (List[int]): List of unique integers from 1 to n with one missing number.
    n (int): The maximum number in the range.

    Returns:
    Tuple[int, bool]: A tuple containing the missing number and a boolean indicating
                      whether it is a power of two.
    """
    # Step 1: Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Step 2: Calculate the actual sum of the array
    actual_sum = sum(nums)
    
    # Step 3: Determine the missing number
    missing_number = expected_sum - actual_sum
    
    # Step 4: Function to check if a number is a power of two
    def is_power_of_two(x):
        return x > 0 and (x & (x - 1)) == 0
    
    # Step 5: Check if the missing number is a power of two
    power_of_two = is_power_of_two(missing_number)
    
    # Return both the missing number and the power of two status
    return missing_number, power_of_two

# Example usage:
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 2, 4, 5, 6, 7, 8]
    n1 = 8
    missing1, is_power1 = find_missing_number_and_check_power_of_two(nums1, n1)
    print(f"Missing Number: {missing1}, Is Power of Two: {is_power1}")  # Output: Missing Number: 3, Is Power of Two: False

    # Example 2
    nums2 = [1, 3, 4, 5, 6, 7, 8]
    n2 = 8
    missing2, is_power2 = find_missing_number_and_check_power_of_two(nums2, n2)
    print(f"Missing Number: {missing2}, Is Power of Two: {is_power2}")  # Output: Missing Number: 2, Is Power of Two: True
