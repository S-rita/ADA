import sys

def merge_and_count(arr, temp, left, mid, right):
    """ Merges two sorted halves of `arr` and counts inversions """
    i, j, k = left, mid + 1, left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:  
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)  # Count inversions
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count

def merge_sort_and_count(arr, temp, left, right):
    """ Recursively sort the array and count inversions """
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        inv_count += merge_and_count(arr, temp, left, mid, right)
    return inv_count

def count_inversions(arr, n):
    """ Wrapper function to count inversions using Merge Sort """
    temp = [0] * n
    return merge_sort_and_count(arr, temp, 0, n - 1)

def main():
    input_data = sys.stdin.read().strip().split("\n")
    
    t = int(input_data[0].strip())  # Read the number of test cases
    index = 1
    
    results = []
    for _ in range(t):
        while index < len(input_data) and input_data[index].strip() == "":  # Skip blank lines
            index += 1
            
        if index >= len(input_data):  # Safety check
            break

        n = int(input_data[index].strip())  # Read `n`
        index += 1
        
        arr = []
        for _ in range(n):
            arr.append(int(input_data[index].strip()))
            index += 1

        results.append(str(count_inversions(arr, n)))

        while index < len(input_data) and input_data[index].strip() == "":  # Skip blank lines again
            index += 1

    print("\n".join(results))  # Print all results efficiently

if __name__ == "__main__":
    main()
