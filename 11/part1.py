from os import path
from functools import cache

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    graph = parse_input()

    @cache
    def paths(start: str, dest: str) -> int:
        if start == dest:
            return 1

        total = 0 
        for option in graph[start]:
            total += paths(option, dest)

        return total

    print(paths('you', 'out'))

def parse_input() -> dict[str, tuple[str]]:
    with open(INPUT_PATH) as f:
        lines = f.read().strip().split('\n')

        devices = []
        for line in lines:
            id, outputs = line.split(': ')
            devices.append((id, tuple(outputs.split())))

        graph = {}
        for id, outputs in devices:
            graph[id] = outputs

        return graph

if __name__ == '__main__':
    main()