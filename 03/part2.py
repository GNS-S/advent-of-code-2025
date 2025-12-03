from part1 import parse_input

def main():
    banks = parse_input()

    ans = []
    for bank in banks:
        digits = 0 
        left = 0
        for i in range(11, -1, -1):
            next_digit = max(bank[left:-i]) if i != 0 else max(bank[left:])
            left += bank[left:].index(next_digit) + 1
            digits = digits * 10 + next_digit

        ans.append(digits)

    print(sum(ans))

if __name__ == '__main__':
    main()