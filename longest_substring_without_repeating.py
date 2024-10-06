def longest_substring_without_repeating(s):
    char_index_map = {}
    left = 0
    max_length = 0
    start_index = 0  # To store the starting index of the longest substring

    for right in range(len(s)):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            # Move the left pointer to the right of the last occurrence of the character
            left = char_index_map[s[right]] + 1
            
        # Update the last seen index of the character
        char_index_map[s[right]] = right
        
        # Update max_length and start_index
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            start_index = left

    # Return the longest substring and its length
    return s[start_index:start_index + max_length], max_length

# Example usage
if __name__ == "__main__":
    input_string = "abcabcbb"
    longest_substr, length = longest_substring_without_repeating(input_string)
    print("Longest substring without repeating characters:", longest_substr)
    print("Length of the substring:", length)
