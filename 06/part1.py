from os import path

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    lines = parse_input()
    ops = lines.pop().split()
    nums = [line.split() for line in lines]
    
    ans = 0
    for i, op in enumerate(ops):
        total = 0 if op == '+' else 1

        for row in nums:
            num = int(row[i])
            total = total + num if op == '+' else total * num

        ans += total
            
    print(ans)

def parse_input() -> list[str]:
    with open(INPUT_PATH) as f:
        lines = f.read().split('\n')
        return lines

if __name__ == '__main__':
    main()