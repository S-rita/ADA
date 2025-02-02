def count_swap(p, count, m):
    if len(p) <= 1 or m == 0:
        return count
    
    front = p[:m]
    back = p[m:]
    
    if sorted(front) != list(range(min(front), max(front) + 1)) or \
       sorted(back) != list(range(min(back), max(back) + 1)):
        return -1
    
    if min(front) > min(back):
        count += 1
        front, back = back, front
    
    left_count = count_swap(front, 0, len(front) // 2)
    right_count = count_swap(back, 0, len(back) // 2)
    
    if left_count == -1 or right_count == -1:
        return -1 
    
    return count + left_count + right_count


n = int(input())
for _ in range(n):
    m = int(input()) // 2
    p = list(map(int, input().split()))
    print(count_swap(p, 0, m))
