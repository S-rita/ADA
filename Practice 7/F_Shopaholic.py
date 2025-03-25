def max_discount(n, prices):
    # Sort the prices in descending order
    prices.sort(reverse=True)
    
    total_discount = 0
    
    # For every 3rd item (0-based index: 2, 5, 8, etc.), it is free
    for i in range(2, n, 3):
        total_discount += prices[i]
    
    return total_discount

# Input handling
n = int(input())  # Number of items Lindsay is buying
prices = list(map(int, input().split()))  # Prices of the items

# Calculate and print the maximum discount Lindsay can get
print(max_discount(n, prices))
