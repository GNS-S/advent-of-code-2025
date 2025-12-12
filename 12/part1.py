from os import path

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    presents, spaces = parse_input()

    ans = 0
    for (width, height), requirements in spaces:
        available_area = width * height
        present_area = 0
        for i, count in enumerate(requirements):
            present_area += sum(row.count('#') for row in presents[i])*count

        if present_area <= available_area:
            ans += 1

    print(ans)
            
def parse_input() -> dict[str, tuple[str]]:
    with open(INPUT_PATH) as f:
        blocks = f.read().strip().split('\n\n')
        present_blocks, space_block = blocks[:-1], blocks[-1]

        presents = []
        for present_block in present_blocks:
            shape = [list(l) for l in present_block.split('\n')[1:]]
            presents.append(shape)

        spaces = []
        for line in space_block.split('\n'):
            shape, requirements_string = line.split(': ')
            width, height = tuple(int(x) for x in shape.split('x'))
            requirements = tuple(int(x) for x in requirements_string.split())
            spaces.append(((width, height), requirements))

        return presents, spaces

if __name__ == '__main__':
    main()