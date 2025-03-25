def store_items(n, m, item_drawers):
    drawers = [False] * m  # False means empty, True means occupied
    results = []
    
    for item in item_drawers:
        d1, d2 = item
        d1 -= 1  # Convert to 0-based indexing
        d2 -= 1  # Convert to 0-based indexing
        
        # Try to store the item
        if not drawers[d1]:  # If drawer d1 is empty, store the item there
            drawers[d1] = True
            results.append("LADICA")
        elif not drawers[d2]:  # If drawer d2 is empty, store the item there
            drawers[d2] = True
            results.append("LADICA")
        else:
            # If both drawers are full, try to find any empty drawer
            found_empty = False
            for i in range(m):
                if not drawers[i]:
                    drawers[i] = True
                    found_empty = True
                    results.append("LADICA")
                    break
            
            # If no empty drawer is found, throw away the item
            if not found_empty:
                results.append("SMECE")
    
    return results

# Read input
n, m = map(int, input().split())
item_drawers = [tuple(map(int, input().split())) for _ in range(n)]

# Store items and print results
result = store_items(n, m, item_drawers)
for res in result:
    print(res)
