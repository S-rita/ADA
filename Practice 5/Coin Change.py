def count_ways_to_make_change(max_amount):
    # Define the coin denominations
    coins = [50, 25, 10, 5, 1]
    
    # Initialize dp array with zero ways to make any amount
    dp = [0] * (max_amount + 1)
    dp[0] = 1  # There is 1 way to make 0 cents (use no coins)
    
    # Process each coin and update the dp array
    for coin in coins:
        for i in range(coin, max_amount + 1):
            dp[i] += dp[i - coin]
    
    return dp

def main():
    # Read input
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # Precompute all possible ways up to 7489 cents
    max_amount = 7489
    dp = count_ways_to_make_change(max_amount)
    
    # Process each input amount
    for line in data:
        if line.strip():
            amount = int(line.strip())
            print(dp[amount])

if __name__ == "__main__":
    main()
