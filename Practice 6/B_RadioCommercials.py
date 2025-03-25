def max_expected_profit(n, p, students):
    profit = [s - p for s in students]

    max_sum = current_sum = profit[0]
    for i in range(1, n):
        current_sum = max(profit[i], current_sum + profit[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

n, p = map(int, input().split())
students = list(map(int, input().split()))

print(max_expected_profit(n, p, students))
