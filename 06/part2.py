from math import prod
from part1 import parse_input

def main():
    lines = parse_input()
    grid = [list(line) for line in lines]
    row_count = len(grid)
    col_count = len(grid[0])

    ans = 0
    operator, operands = None, []
    for c in range(col_count - 1, -1, -1):
        num = ''
        for r in range(row_count):
            char = grid[r][c]
            if char.isdigit():
                num += char
            elif char == '+':
                operator = sum
            elif char == '*':
                operator = prod

        if num != '':
            operands.append(int(num))

        if operator != None:
            ans += operator(operands)
            operator, operands = None, []

    print(ans)

if __name__ == '__main__':
    main()