from part1 import parse_input
from functools import cache

def main():
    graph = parse_input()

    @cache
    def paths(start: str, dest: str, saw_dac=False, saw_fft=False) -> int:
        if start == dest:
            return 1 if saw_dac and saw_fft else 0
        
        total = 0 
        for option in graph[start]:
            total += paths(
                option,
                dest,
                saw_dac=saw_dac or start == 'dac',
                saw_fft=saw_fft or start == 'fft'
            )

        return total

    print(paths('svr', 'out'))

if __name__ == '__main__':
    main()