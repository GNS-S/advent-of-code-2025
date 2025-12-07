from part1 import parse_input
from functools import cache

def main():
    grid = parse_input()
    final_row_index = len(grid) - 1
    start_r = 0
    start_c = grid[start_r].index('S')

    @cache
    def beam(row: int, col: int):
        if row == final_row_index:
            return 1
        if grid[row][col] == '^':
            return beam(row, col - 1) + beam(row, col + 1)
        
        return beam(row + 1, col)

    print(beam(start_r, start_c))

if __name__ == '__main__':
    main()