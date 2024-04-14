def candies(n, arr):
    # Initialize an array to store the number of candies for each child
    candy_counts = [1] * n

    # Traverse from left to right
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candy_counts[i] = candy_counts[i - 1] + 1

    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candy_counts[i] = max(candy_counts[i], candy_counts[i + 1] + 1)

    # Return the total number of candies needed
    return sum(candy_counts)

# Example usage
n = 4
arr = [3, 1, 2, 2]
result = candies(n, arr)
print("Minimum number of candies:", result)
