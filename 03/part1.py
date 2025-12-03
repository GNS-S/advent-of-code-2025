from os import path

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    banks = parse_input()

    ans = 0
    for bank in banks:
        left = max(bank[:-1])
        right = max(bank[bank.index(left) + 1:])

        ans += left*10 + right
            
    print(ans)


def parse_input() -> list[list[int]]:
    with open(INPUT_PATH) as f:
        lines = f.read().strip().split('\n')

        banks = []
        for line in lines:
            banks.append([int(x) for x in list(line)])

        return banks

if __name__ == '__main__':
    main()