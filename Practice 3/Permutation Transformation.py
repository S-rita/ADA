def depth(p, ans, d):
    if len(ans) == 0:
        return []
    if len(ans) == 1:
        ans[0] = d
        return ans
    else:
        ind = p.index(max(p))
        ans[ind] = d
        ans[:ind] = depth(p[:ind], ans[:ind], d+1)
        d = ans[ind]
        ans[ind+1:] = depth(p[ind+1:], ans[ind+1:], d+1)
        return ans

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    ans = depth(p, p, 0)
    for i in ans:
        print(i, end=" ")
