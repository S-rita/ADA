import sys
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def brute_force(points):
    min_dist = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                closest_pair = (points[i], points[j])
    return closest_pair, min_dist

def closest_pair_recursive(points_sorted_x, points_sorted_y):
    n = len(points_sorted_x)
    if n <= 3:
        return brute_force(points_sorted_x)
    
    mid = n // 2
    mid_point = points_sorted_x[mid]
    
    left_x = points_sorted_x[:mid]
    right_x = points_sorted_x[mid:]
    left_y = list(filter(lambda p: p[0] <= mid_point[0], points_sorted_y))
    right_y = list(filter(lambda p: p[0] > mid_point[0], points_sorted_y))
    
    (p1, q1), d1 = closest_pair_recursive(left_x, left_y)
    (p2, q2), d2 = closest_pair_recursive(right_x, right_y)
    
    if d1 < d2:
        d_min = d1
        best_pair = (p1, q1)
    else:
        d_min = d2
        best_pair = (p2, q2)
    
    strip = [p for p in points_sorted_y if abs(p[0] - mid_point[0]) < d_min]
    
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            d = distance(strip[i], strip[j])
            if d < d_min:
                d_min = d
                best_pair = (strip[i], strip[j])
    
    return best_pair, d_min

def closest_pair(points):
    points_sorted_x = sorted(points)
    points_sorted_y = sorted(points, key=lambda p: p[1])
    return closest_pair_recursive(points_sorted_x, points_sorted_y)[0]

def main():
    input_data = sys.stdin.read().strip().split('\n')
    index = 0
    results = []
    while index < len(input_data):
        n = int(input_data[index])
        if n == 0:
            break
        points = []
        for i in range(n):
            x, y = map(float, input_data[index + i + 1].split())
            points.append((x, y))
        index += n + 1
        p1, p2 = closest_pair(points)
        results.append(f"{p1[0]} {p1[1]} {p2[0]} {p2[1]}")
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
