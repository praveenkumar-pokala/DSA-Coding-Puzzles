def num_islands(grid):
    if not grid:
        return 0
    
    # Get dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    # Helper function to perform DFS and mark visited lands
    def dfs(r, c):
        # Check for out-of-bound indices or if the cell is already visited (water)
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        # Mark the current cell as visited by setting it to '0'
        grid[r][c] = '0'
        
        # Visit all adjacent cells (up, down, left, right)
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right

    # Traverse the entire grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # If the cell is land ('1')
                island_count += 1   # Increment the count of islands
                dfs(r, c)           # Perform DFS to mark the entire island

    return island_count

# Example usage
if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print("Number of islands:", num_islands(grid))
