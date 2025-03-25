import sys

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size  # Using rank instead of size for optimization

    def find(self, index):
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])  # Path compression
        return self.parent[index]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:  # Union by rank
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def main():
    input_data = sys.stdin.read().splitlines()
    length, lines = map(int, input_data[0].split())

    uf = UnionFind(length)
    result = []

    for i in range(1, lines + 1):
        line = input_data[i].split()
        a, b = int(line[1]), int(line[2])

        if line[0] == "=":
            uf.union(a, b)
        elif line[0] == "?":
            result.append("yes" if uf.find(a) == uf.find(b) else "no")

    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()
