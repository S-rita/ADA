def find_lexicographically_earliest_lis(sequence):
    n = len(sequence)
    lis = []
    index_tracker = [-1] * n  # Stores previous indices for LIS reconstruction
    parent = [-1] * n  # To reconstruct the sequence
    
    for i, num in enumerate(sequence):
        pos = 0
        while pos < len(lis) and lis[pos] < num:
            pos += 1
        
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
        
        index_tracker[pos] = i  # Store index of current element
        if pos > 0:
            parent[i] = index_tracker[pos - 1]  # Link to previous LIS element
    
    # Reconstruct the LIS sequence
    lis_sequence = []
    last_index = index_tracker[len(lis) - 1]
    while last_index != -1:
        lis_sequence.append(sequence[last_index])
        last_index = parent[last_index]
    
    return len(lis), lis_sequence[::-1]

def main():
    while True:
        line = input().strip()
        if line == "0":
            break
        
        values = list(map(int, line.split()))
        n = values[0]
        sequence = values[1:]
        
        length, lis_sequence = find_lexicographically_earliest_lis(sequence)
        print(length, *lis_sequence)

if __name__ == "__main__":
    main()
