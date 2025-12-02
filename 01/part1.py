from os import path

def main():
    INPUT_DIR = path.dirname(path.realpath(__file__))
    INPUT_PATH = f'{INPUT_DIR}/input.txt'

    with open(INPUT_PATH) as f:
        rotations = parse_input(f)

        ans = 0
        pos = 50
        for dir, amount in rotations:
            diff = -amount if dir == 'L' else amount
            pos += diff
            if pos % 100 == 0:
                ans += 1
    print(ans)


def parse_input(file) -> list[tuple[str, int]]:
    lines = file.read().strip().split('\n')

    rotations = []
    for line in lines:
        direction, amount  = line[:1], line[1:]
        rotations.append((direction, int(amount)))

    return rotations

if __name__ == '__main__':
    main()