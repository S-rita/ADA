def max_team_performance(datasets):
    results = []
    
    for n, scores in datasets:
        scores.sort(reverse=True)  # Sort scores in descending order
        
        # Select every second student from the last 2n elements
        total_performance = sum(scores[i] for i in range(1, 2 * n + 1, 2))
        
        results.append(total_performance)
    
    return results

# Input Handling
t = int(input())  # Number of datasets
datasets = []

for _ in range(t):
    n = int(input())  # Number of teams
    scores = list(map(int, input().split()))  # Scores of 3n students
    datasets.append((n, scores))

# Compute and print results for each dataset
for result in max_team_performance(datasets):
    print(result)
