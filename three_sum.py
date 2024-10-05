def three_sum(nums, target):
    # Sort the input array
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Avoid duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Initialize two pointers
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # Avoid duplicates for the second number
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Avoid duplicates for the third number
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result

# Example usage
example_array = [-1, 0, 1, 2, -1, -4]
target_sum = 0
triplets = three_sum(example_array, target_sum)

print(f"Triplets that sum to {target_sum}:", triplets)  # Output: Triplets that sum to 0: [[-1, -1, 2], [-1, 0, 1]]
