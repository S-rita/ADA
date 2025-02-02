def min_moves_to_good_string(test_cases):
    def helper(s, c):
        n = len(s)
        if n == 1:
            return 0 if s[0] == c else 1
        
        mid = n // 2
        left = s[:mid]
        right = s[mid:]
        
        left_cost = helper(right, chr(ord(c) + 1)) + (mid - left.count(c))
        right_cost = helper(left, chr(ord(c) + 1)) + (mid - right.count(c))
        
        return min(left_cost, right_cost)

    results = []
    for n, s in test_cases:
        results.append(helper(s, 'a'))
    return results

t = int(input())  
test_cases = []
for _ in range(t):
    n = int(input()) 
    s = input()  
    test_cases.append((n, s))

results = min_moves_to_good_string(test_cases)
for res in results:
    print(res)
