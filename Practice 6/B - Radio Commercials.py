def max_profit(n, p, students):
    net_profit = [students[i] - p for i in range(n)]
    
    max_sum = float('-inf')
    current_sum = 0
    
    for value in net_profit:
        current_sum = max(value, current_sum + value)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

n, p = map(int, input().split())
students = list(map(int, input().split()))

print(max_profit(n, p, students))
