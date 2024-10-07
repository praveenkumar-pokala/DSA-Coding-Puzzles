def egg_drop(n, k):
    # A 2D table where entry dp[i][j] will represent minimum number of trials 
    # needed for i eggs and j floors.
    dp = [[0 for x in range(k+1)] for x in range(n+1)]

    # We need one trial for one floor and zero trials for zero floors.
    for i in range(1, n+1):
        dp[i][1] = 1  # One floor
        dp[i][0] = 0  # Zero floors

    # We need j trials for one egg and j floors.
    for j in range(1, k+1):
        dp[1][j] = j

    # Fill the rest of the table using the optimal substructure property.
    for i in range(2, n+1):
        for j in range(2, k+1):
            dp[i][j] = float('inf')  # Initialize with infinity
            for x in range(1, j+1):
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(dp[i][j], res)

    # The answer will be in dp[n][k]
    return dp[n][k]

# Example usage:
eggs = 2
floors = 10
print("Minimum number of trials needed:", egg_drop(eggs, floors))
