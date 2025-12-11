from os import path
from itertools import combinations

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    coords = parse_input()

    ans = 0
    for a, b in combinations(coords, 2):
        area = rectangle_area(a, b)
        ans = max(ans, area)

    print(ans)

def parse_input() -> list[tuple[int, int]]:
    with open(INPUT_PATH) as f:
        lines = f.read().strip().split('\n')

        coords = []
        for line in lines:
            x, y = line.split(',')
            coords.append((int(x), int(y)))

        return coords
    
def rectangle_area(a: tuple[int, int], b: tuple[int, int]) -> int:
    x, y = a
    x2, y2 = b
    return (abs(x2 - x) + 1) * (abs(y2 - y) + 1)
    
if __name__ == '__main__':
    main()