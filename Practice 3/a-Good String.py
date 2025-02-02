def count_move(word, ch, n):
    if n == 1: 
        return 0 if word[0] == ch else 1
    else:
        half = n // 2
        left_mismatch = sum(1 for i in range(half) if word[i] != ch)
        right_mismatch = sum(1 for i in range(half, n) if word[i] != ch)
        return min(
            left_mismatch + count_move(word[half:], chr(ord(ch) + 1), half),
            right_mismatch + count_move(word[:half], chr(ord(ch) + 1), half),
        )

t = int(input())
for _ in range(t):
    n = int(input())
    word = input()
    print(count_move(word, "a", n))
