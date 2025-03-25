def max_tasks_completed(n, m, task_durations, quiet_intervals):
    # Step 1: Sort tasks and quiet intervals in ascending order
    task_durations.sort()
    quiet_intervals.sort()

    # Step 2: Use two-pointer technique to assign tasks
    i, j, count = 0, 0, 0  # i -> task index, j -> quiet interval index

    while i < n and j < m:
        if task_durations[i] <= quiet_intervals[j]:  # Task fits into the interval
            count += 1
            i += 1  # Move to next task
        j += 1  # Always move to next interval

    return count

# Input Handling
n, m = map(int, input().split())  # Read number of tasks and quiet intervals
task_durations = list(map(int, input().split()))  # Read task durations
quiet_intervals = list(map(int, input().split()))  # Read quiet interval durations

# Compute and print the maximum number of tasks that can be completed
print(max_tasks_completed(n, m, task_durations, quiet_intervals))
