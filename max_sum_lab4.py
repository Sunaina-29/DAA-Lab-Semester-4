def maximize_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()

    # Initialize max_sum
    max_sum = 0

    # Iterate through the sorted array and calculate max_sum
    for i, num in enumerate(arr):
        max_sum += num * i

    return max_sum

# Example usage
arr = [2, 5, 3, 4, 0]
result = maximize_sum(arr)
print("Maximum sum:", result)
