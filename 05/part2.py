from part1 import parse_input

def main():
    ranges, _ = parse_input()
    ranges.sort()

    merged = [ranges.pop(0)]
    for s2, e2 in ranges:
        s1, e1 = merged[-1]

        if s2 > e1:
            merged.append((s2, e2))
        else: 
            new_s = min(s1, s2)
            new_e = max(e1, e2)
            merged[-1] = (new_s, new_e)

    ans = 0
    for s,  e in merged:
        ans += e - s + 1

    print(ans)

if __name__ == '__main__':
    main()