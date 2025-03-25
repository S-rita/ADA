import sys
sys.setrecursionlimit(10000)

def find_bridges(n, adj):
    discovery_time = [-1] * n
    low_time = [-1] * n
    parent = [-1] * n
    time = [0]  # Mutable counter to track discovery times
    bridges = []
    
    def dfs(u):
        discovery_time[u] = low_time[u] = time[0]
        time[0] += 1
        for v in adj[u]:
            if discovery_time[v] == -1:  # If v is not visited
                parent[v] = u
                dfs(v)
                low_time[u] = min(low_time[u], low_time[v])
                # If the lowest point reachable from v is greater than u's discovery time, then (u, v) is a bridge
                if low_time[v] > discovery_time[u]:
                    bridges.append((u, v))
            elif v != parent[u]:  # Back edge and not the parent edge
                low_time[u] = min(low_time[u], discovery_time[v])
    
    # Start DFS from all nodes that are unvisited
    for i in range(n):
        if discovery_time[i] == -1:
            dfs(i)
    
    return bridges

def solve(test_cases):
    results = []
    
    for case in test_cases:
        n, m, edges = case
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        bridges = find_bridges(n, adj)
        
        if bridges:
            results.append("Yes")
        else:
            results.append("No")
    
    return results

def main():
    test_cases = []
    
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        test_cases.append((n, m, edges))
    
    results = solve(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
