from os import path

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    ranges, ingredients = parse_input()

    ans = 0
    for ingredient in ingredients:
        for x1, x2 in ranges:
            if x1 <= ingredient <= x2:
                ans += 1
                break

    print(ans)

def parse_input() -> list[list[str]]:
    with open(INPUT_PATH) as f:
        range_lines, ingredient_lines = f.read().strip().split('\n\n')

        ranges = []
        for line in range_lines.split():
            start, end = line.split('-')
            ranges.append((int(start), int(end)))

        ingredients = []
        for line in ingredient_lines.split():
            ingredients.append(int(line))

        return ranges, ingredients

if __name__ == '__main__':
    main()