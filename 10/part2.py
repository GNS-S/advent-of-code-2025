from part1 import parse_input
from math import gcd, inf

def main():
    machines = parse_input()
    ans = 0

    for _, buttons, joltages in machines:
        # Represent the problem as a system of linear equations
        # Ax = b
        #
        # A is a len(joltages) x len(buttons) matrix
        # A[i][j]=1 - when button j is pressed joltage counter i is incremented by 1
        #
        # b is a len(joltages) column vector - the input array of joltages
        #
        # x is a len(buttons) column vector - press counts for each button
        A = [[1 if i in button else 0 for button in buttons] for i in range(len(joltages))]
        b = list(joltages)

        # Reduce A and b to RREF and swap columns to ensure that the diagonal is fully populated and
        # all free variables (if there's any) lie in columns to the right of the last value of the
        # diagonal (col index > matrix rank - 1)
        #
        # Also take note of the the new column (button) order after swaps
        A, b, col_order = permuted_rref(A, b)
  
        # bounds is a len(buttons) row vector, bounds[i] - maximum times button i can be presssed
        bounds = [min([joltages[i] for i in buttons[button_i]]) for button_i in col_order]

        # Go through all free variable combinations and find the min sum
        row_count = len(A)
        col_count = len(A[0])
        fvar_count = col_count - row_count
        fvar_combs = bounded_combinations(bounds[-fvar_count:]) if fvar_count > 0 else [[]]

        min_sum = inf
        for fvars in fvar_combs:
            min_sum = min(min_sum, solve_sum(A, b, fvars) + sum(fvars))

        ans += min_sum

    print(ans)

def permuted_rref(A, b):
    row_count = len(A)
    col_count = len(A[0])
    col_order = [i for i in range(col_count)]

    def _reduce_row(pivot: int, r: int):
        '''
        Eliminate value A[r][pivot] and mutate A and b accordingly
        '''
        if A[pivot][pivot] == 0 or A[r][pivot] == 0:
            return

        factor_p = -A[r][pivot]
        factor_r = A[pivot][pivot]
        divisor = gcd(factor_r, factor_p)
        factor_p //= divisor
        factor_r //= divisor

        A[r] = [factor_p * A[pivot][c] + factor_r * A[r][c] for c in range(col_count)]
        b[r] = factor_p * b[pivot] + factor_r * b[r]

    # Reduce matrix A to REF
    for pivot in range(col_count):
        # Find the first non-zero value we can place in A[pivot][pivot]
        # It cannot be from rows or colums with lower indexes than pivot - they're already reduced
        for swap_c in range(pivot, col_count):
            swap_r = next((r for r in range(pivot, row_count) if A[r][swap_c] != 0), None)
            if swap_r != None:
                break

        # Can't find value - done
        if swap_r == None:
            break

        if swap_c != pivot:
            for r in range(row_count):
                A[r][pivot], A[r][swap_c] = A[r][swap_c], A[r][pivot]
            col_order[pivot], col_order[swap_c] = col_order[swap_c], col_order[pivot]

        if swap_r != pivot:
            A[pivot], A[swap_r] = A[swap_r], A[pivot]
            b[pivot], b[swap_r] = b[swap_r], b[pivot]

        # Eliminate rows below pivot
        for r in range(pivot + 1, row_count):
            _reduce_row(pivot, r)

    # Filter out empty - all 0 - rows
    for r in range(row_count - 1, -1, -1):
        if all(x == 0 for x in A[r]):
            A.pop(r)
            b.pop(r)
    row_count = len(A)
          
    # RREF - eliminate rows above pivot
    for pivot in range(row_count-1, -1, -1):
        for r in range(pivot):
            _reduce_row(pivot, r)

    return A, b, col_order


def bounded_combinations(bounds: list[int]) -> list[tuple]:
    '''
    Return list of positive integer combinations such that for every combination:
    combination[i] <= bounds[i]
    '''
    combinations: list[tuple] = []
    Q = [tuple()]
    while Q:
        sofar = Q.pop()
        if len(sofar) == len(bounds):
            combinations.append(sofar)
            continue
        
        for i in range(bounds[len(sofar)] + 1):
            Q.append((*sofar, i))

    return combinations

def solve_sum(A: list[list[int]], b: list[int], fvars: list[int]):
    '''
    Solves for sum of xs for Ax = b. Return inf for impossible xs
    
    :param A: matrix in RREF, populated diagonal and all free variables in column indices > rank(A)
    :param b: rhs column vector
    :param fvars: free variables to substitute
    '''
    row_count = len(A)
    col_count = len(A[0])
    fvar_count = col_count - row_count

    x_sum = 0
    for r in range(row_count):
        fvar_sum = 0
        for i in range(fvar_count):
            fvar_sum += fvars[i] * A[r][col_count - fvar_count + i]

        rhs = b[r] - fvar_sum
        x = rhs / A[r][r]

        # Non-integer and negative solutions are invalid
        if not x.is_integer() or x < 0:
            return inf

        x_sum += int(x)

    return x_sum

if __name__ == '__main__':
    main()
