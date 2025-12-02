from part1 import parse_input

def main():
    ranges = parse_input()

    ans = set()
    for start, end in ranges:
        for num in range(start, end + 1):
            s = str(num)

            for i in range(1, len(s) // 2 + 1):
                repeats = len(s) // i
                if s[:i] * repeats == s:
                    if num not in ans: print(num)
                    ans.add(num)
            
    print(sum(ans))

if __name__ == '__main__':
    main()