def k_sum(nums, target, k):
    def two_sum(nums, target):
        # Two-pointer approach for 2-sum
        res = []
        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        return res

    def k_sum_recursive(nums, target, k):
        res = []
        if not nums:
            return res
        
        # Base case: k == 2, solve using the two-pointer approach
        if k == 2:
            return two_sum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                # Recursively solve (k-1)-sum problem
                for subset in k_sum_recursive(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)
        
        return res

    # Sort the numbers to ensure easier handling of duplicates and two-pointer technique
    nums.sort()
    return k_sum_recursive(nums, target, k)

# Example usage:
if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    k = 4
    result = k_sum(nums, target, k)
    print("K-Sum Results:", result)
