from os import path

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    diagrams = parse_input()

    ans = 0
    for goal, buttons, _ in diagrams:
        initial_state = tuple(False for _ in goal)
        Q = [(initial_state, 0)]
        seen = set()

        while Q:
            state, turns = Q.pop(0)
            if state == goal:
                ans += turns
                break

            if state in seen:
                continue
            seen.add(state)

            for button in buttons:
                new_state = list(state)
                for i in button:
                    new_state[i] = not new_state[i]
                Q.append((tuple(new_state), turns + 1))

    print(ans)

def parse_input() -> list[tuple[tuple, tuple, tuple]]:
    with open(INPUT_PATH) as f:
        lines = f.read().strip().split('\n')
        machines = []
        for line in lines:
            chunks = line.split()
            indicator = tuple(True if c == '#' else False for c in chunks[0][1:-1])
            joltages = tuple(int(c) for c in chunks[-1][1:-1].split(','))

            buttons = []
            for chunk in chunks[1:-1]:
                buttons.append(tuple(int(c) for c in chunk[1:-1].split(',')))

            machines.append((indicator, buttons, joltages))

        return machines

if __name__ == '__main__':
    main()