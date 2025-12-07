from part1 import parse_input
from collections import defaultdict

def main():
    start_col, grid = parse_input()
    beams = defaultdict(int)
    beams[start_col] = 1

    for row in grid:
        for c, tile in enumerate(row):
            if tile == '^' and c in beams:
                beams[c - 1] += beams[c]
                beams[c + 1] += beams[c]
                del beams[c]

    print(sum(beams.values()))

if __name__ == '__main__':
    main()