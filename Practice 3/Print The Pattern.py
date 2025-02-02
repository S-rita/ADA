n = int(input().strip())

word = ["A"]
char = "A"

for _ in range(2, n + 1):
    char = chr(ord(char) + 1)
    word.append(char)
    word.extend(word[:-1])

print("".join(word), end="")
