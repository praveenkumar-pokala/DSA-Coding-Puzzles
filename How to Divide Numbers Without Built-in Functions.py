def divide(dividend, divisor):
    # Handle division by zero
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    
    negative = (dividend < 0) != (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    
    return -quotient if negative else quotient

# Example usage
result = divide(10, 3)
