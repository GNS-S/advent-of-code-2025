from os import path

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    ranges = parse_input()

    ans = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            s = str(num)
            half = len(s) // 2
            if s[:half] == s[half:]:
                ans += num
            
    print(ans)


def parse_input() -> list[tuple[int, int]]:
    with open(INPUT_PATH) as f:
        lines = f.read().strip().split(',')

        ranges = []
        for line in lines:
            start, end  = line.split('-')
            ranges.append((int(start), int(end)))

        return ranges

if __name__ == '__main__':
    main()