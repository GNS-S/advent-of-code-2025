from part1 import parse_input, can_remove

def main():
    grid = parse_input()
    max_r = len(grid) - 1
    max_c = len(grid[0]) - 1

    ans = 0

    while True:
        to_remove = []
        for r in range(max_r + 1):
            for c in range(max_c + 1):
                if grid[r][c] == '@' and can_remove(grid, r, c):
                    to_remove.append((r, c))

        if len(to_remove) == 0:
            break

        for r, c in to_remove:
            grid[r][c] = '.'
        
        ans += len(to_remove)
                   
    print(ans)

if __name__ == '__main__':
    main()