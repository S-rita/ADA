def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        items = []
        max_weight = 0
        
        # Read items
        for _ in range(n):
            value, weight = map(int, input().split())
            items.append((value, weight))
        
        # Read number of weight queries
        m = int(input())
        weights = []
        
        # Read and store all weights, track maximum
        for _ in range(m):
            w = int(input())
            weights.append(w)
            max_weight = max(max_weight, w)
        
        # Create DP table
        # dp[i][w] represents max value using first i items with weight limit w
        dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
        
        # Fill DP table
        for i in range(1, n + 1):
            value, weight = items[i-1]
            for w in range(max_weight + 1):
                # Don't take item i
                dp[i][w] = dp[i-1][w]
                
                # Take item i if possible
                if w >= weight:
                    dp[i][w] = max(dp[i][w], dp[i-1][w - weight] + value)
        
        # Calculate total for all weight queries
        total = 0
        for weight in weights:
            total += dp[n][weight]
            
        print(total)

# Run the solution
solve()
