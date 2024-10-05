def square_root_binary_search(number, precision):
    if number < 0:
        return None  # Square root of a negative number is not real
    
    # Setting the search range
    low = 0
    high = number if number >= 1 else 1  # For numbers < 1, we set the high as 1
    mid = 0
    
    # Binary search to find the square root up to the integer part
    while high - low > 10 ** (-precision):
        mid = (low + high) / 2
        if mid * mid > number:
            high = mid
        else:
            low = mid

    # Formatting the result to the specified precision
    return round(mid, precision)


# Example Usage:
number = 50  # Number to find the square root of
precision = 5  # Number of decimal places

sqrt_result = square_root_binary_search(number, precision)
print(f"Square root of {number} up to {precision} decimal places is: {sqrt_result}")
