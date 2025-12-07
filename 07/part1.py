from os import path

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    grid = parse_input()
    start = grid[0].index('S')

    beams = set([start])

    ans = 0
    for row in grid:
        split_beams = set()
        for r, tile in enumerate(row):
            if tile == '^' and r in beams:
                ans += 1
                beams.remove(r)
                split_beams.add(r - 1)
                split_beams.add(r + 1)

        beams = split_beams.union(beams)

    print(ans)

def parse_input() -> tuple[int, list[list[str]]]:
    with open(INPUT_PATH) as f:
        lines = f.read().strip().split('\n')
        return [list(row) for row in lines]

if __name__ == '__main__':
    main()