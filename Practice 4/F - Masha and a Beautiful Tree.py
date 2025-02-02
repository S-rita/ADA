def calculate_min_swaps(array, start_idx, end_idx):
    if end_idx - start_idx == 1:
        return 0, [array[start_idx]]
    mid_idx = (start_idx + end_idx) // 2
    left_swaps, left_sorted = calculate_min_swaps(array, start_idx, mid_idx)
    right_swaps, right_sorted = calculate_min_swaps(array, mid_idx, end_idx)

    if left_swaps == -1 or right_swaps == -1:
        return -1, []
    if left_sorted[-1] < right_sorted[0]:
        return left_swaps + right_swaps, left_sorted + right_sorted
    elif right_sorted[-1] < left_sorted[0]:
        return left_swaps + right_swaps + 1, right_sorted + left_sorted
    else:
        return -1, []

def main():
    test_cases = int(input())
    results = []
    for _ in range(test_cases):
        array_size = int(input())
        permutation = list(map(int, input().split()))
        swaps, _ = calculate_min_swaps(permutation, 0, array_size)
        results.append(swaps)

    print("\n".join(map(str, results)))

main()
