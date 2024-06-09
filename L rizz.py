import math
import sys

def parse_input():
    planes = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            coord_part, name = line.split(":")
            x_str, y_str = coord_part.split(",")
            x = float(x_str.strip())
            y = float(y_str.strip())
            name = name.strip()
            planes.append((x, y, name))
        except ValueError:
            print("Nespravny vstup.")
            sys.exit(1)
    
    if len(planes) < 2:
        print("Nespravny vstup.")
        sys.exit(1)
    
    return planes

def compute_distances(planes):
    distances = []
    n = len(planes)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, name1 = planes[i]
            x2, y2, name2 = planes[j]
            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            distances.append((distance, planes[i], planes[j]))
    return distances

def find_min_distance_pairs(distances):
    min_distance = min(distances, key=lambda x: x[0])[0]
    min_distance_pairs = [pair for pair in distances if pair[0] == min_distance]
    return min_distance, min_distance_pairs

def main():
    planes = parse_input()
    distances = compute_distances(planes)
    min_distance, min_distance_pairs = find_min_distance_pairs(distances)

    print(f"Vzdalenost nejblizsich letadel: {min_distance:.6f}")
    print(f"Nalezenych dvojic: {len(min_distance_pairs)}")
    
    for _, (x1, y1, name1), (x2, y2, name2) in min_distance_pairs:
        print(f"{name1} - {name2}")

if __name__ == "__main__":
    main()
