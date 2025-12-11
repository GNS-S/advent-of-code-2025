from part1 import parse_input
from scipy.optimize import linprog

def main():
    diagrams = parse_input()

    ans = 0
    for _, buttons, joltage in diagrams:

        # A[i][j] - True if joltage at index i is affected by button at index j
        A_eq = []
        for i in range(len(joltage)):
            A_eq.append([])
            for button in buttons:
                A_eq[-1].append(1 if i in button else 0)

        c = [1 for _ in buttons]
        b_eq = joltage
        ans += linprog(c, A_eq=A_eq, b_eq=b_eq, integrality=1).fun

    print(int(ans))

if __name__ == '__main__':
    main()