def max_even_position_sum(test_cases):
    results = []
    for n, a in test_cases:
        initial_sum = sum(a[i] for i in range(0, n, 2))
        
        max_gain = 0
        gain = 0
        for i in range(1, n, 2):
            gain += a[i] - (a[i - 1] if i - 1 >= 0 else 0)
            if gain < 0:
                gain = 0
            max_gain = max(max_gain, gain)
        
        gain = 0
        for i in range(2, n, 2):
            gain += a[i - 1] - a[i]
            if gain < 0:
                gain = 0
            max_gain = max(max_gain, gain)
        
        results.append(initial_sum + max_gain)
    
    return results


t = int(input()) 
test_cases = []
for _ in range(t):
    n = int(input()) 
    a = list(map(int, input().split()))  
    test_cases.append((n, a))

results = max_even_position_sum(test_cases)
for res in results:
    print(res)
