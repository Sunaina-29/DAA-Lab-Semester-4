def minimize_product_sum(array_One, array_Two):
    # Sort both arrays
    array_One.sort()
    array_Two.sort(reverse=True)  # Sort in reverse order

    # Initialize the sum of products
    min_sum = 0

    # Multiply elements pairwise and sum them up
    for i in range(len(array_One)):
        min_sum += array_One[i] * array_Two[i]

    return min_sum

# Example usage
array_One = [7, 5, 1, 4]
array_Two = [6, 17, 9, 3]
result = minimize_product_sum(array_One, array_Two)
print("Minimum sum of product of pairs:", result)
