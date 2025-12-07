from os import path

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    grid = parse_input()
    ans = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@' and can_remove(grid, r, c):
                ans += 1
                   
    print(ans)

def can_remove(grid: list[list[str]], r: int, c: int) -> bool:
    max_r = len(grid) - 1
    max_c = len(grid[0]) - 1
    directions = [
        (-1,  0),
        (-1,  1),
        ( 0,  1),
        ( 1,  1),
        ( 1,  0),
        ( 1, -1),
        ( 0, -1),
        (-1, -1),
    ]

    adjacement = 0
    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        in_bounds = 0 <= new_r <= max_r and 0 <= new_c <= max_c
        if in_bounds and grid[new_r][new_c] == '@':
            adjacement += 1

    return adjacement < 4

def parse_input() -> list[list[str]]:
    with open(INPUT_PATH) as f:
        lines = f.read().strip().split('\n')
        rows = []
        for line in lines:
            rows.append(list(line))
        return rows

if __name__ == '__main__':
    main()