DP = [[[0 for _ in range(352)] for _ in range(27)] for _ in range(27)]

def solve():
    DP[0][0][0] = 1
    for letter in range(1, 27): 
        for max_length in range(0, letter + 1): 
            for sum in range(352): 
                DP[letter][max_length][sum] = DP[letter - 1][max_length][sum]
                if max_length > 0 and sum >= letter:
                    DP[letter][max_length][sum] += DP[letter - 1][max_length - 1][sum - letter]

if __name__ == "__main__":
    solve()
    case_number = 0
    while True:

        line = input().strip()
        if not line:
            break
        L, S = map(int, line.split())
        
        if L == 0 and S == 0:
            break

        case_number += 1
        print(f"Case {case_number}: ", end="")
        if L > 26 or S > 351:
            print("0")
        else:
            print(DP[26][L][S])
