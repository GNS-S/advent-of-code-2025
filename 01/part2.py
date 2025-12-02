from part1 import parse_input

def main():
    rotations = parse_input()

    ans = 0
    pos = 50
    for dir, amount in rotations:
        ans += amount // 100
        amount %= 100

        diff = -amount if dir == 'L' else amount

        new_pos = pos + diff

        if new_pos < 0:
            if pos != 0:
                ans += 1
            new_pos = 100 + new_pos
        elif new_pos >= 100:
            ans += 1
            new_pos %= 100
        elif new_pos == 0:
            ans += 1
        pos = new_pos

    print(ans)

if __name__ == '__main__':
    main()