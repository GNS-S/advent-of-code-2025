from os import path

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    coords = parse_input()

    ans = 0
    for i in range(len(coords)):
        for j in range(i, len(coords)):
            area = square_area(coords[i], coords[j])
            ans = max(ans, area)

    print(ans)

def parse_input() -> tuple[int, list[list[str]]]:
    with open(INPUT_PATH) as f:
        lines = f.read().strip().split('\n')

        coords = []
        for line in lines:
            x, y = line.split(',')
            coords.append((int(x), int(y)))

        return coords
    
def square_area(a: tuple[int, int], b: tuple[int, int]) -> int:
    x, y = a
    x2, y2 = b
    return (abs(x2 - x) + 1) * (abs(y2 - y) + 1)
    
if __name__ == '__main__':
    main()