def fractional_knapsack(items, capacity):
    # Calculate the ratio of benefit to weight for each item
    for item in items:
        item['ratio'] = item['benefit'] / item['weight']
    
    # Sort items based on the ratio in decreasing order
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_benefit = 0
    total_weight = 0
    knapsack = []

    for item in items:
        if total_weight + item['weight'] <= capacity:
            # Add the whole item to the knapsack
            knapsack.append(item)
            total_weight += item['weight']
            total_benefit += item['benefit']
        else:
            # Add a fraction of the item to fill the knapsack
            remaining_capacity = capacity - total_weight
            fraction = remaining_capacity / item['weight']
            item['fraction'] = fraction
            knapsack.append(item)
            total_weight += remaining_capacity
            total_benefit += fraction * item['benefit']
            break  # Knapsack is full
        
    return knapsack, total_benefit

# Example usage
items = [
    {'benefit': 60, 'weight': 10},
    {'benefit': 100, 'weight': 20},
    {'benefit': 120, 'weight': 30}
]
capacity = 50

optimal_solution, total_benefit = fractional_knapsack(items, capacity)

print("Optimal solution:")
for item in optimal_solution:
    if 'fraction' in item:
        print(f"Item with benefit {item['benefit']} and weight {item['weight']}, fraction used: {item['fraction']}")
    else:
        print(f"Item with benefit {item['benefit']} and weight {item['weight']}")
print("Total benefit:", total_benefit)
