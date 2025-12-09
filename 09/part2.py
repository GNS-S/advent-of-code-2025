from heapq import heappop, heappush
from part1 import parse_input, square_area

def main():
    coords = parse_input()

    area_heap = []

    for i in range(len(coords)):
        for j in range(i, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            
            topleft = min(x1, x2), min(y1, y2)
            botright = max(x1, x2), max(y1, y2)
            area = square_area(coords[i], coords[j])

            heappush(area_heap, (-area, topleft, botright))

    ans = None
    while area_heap and ans == None:
        negative_area, topleft, botright = heappop(area_heap)
        ans = -negative_area
        for i in range(len(coords)):
            j = (i + 1) % len(coords)

            tlx, tly = topleft
            brx, bry = botright
            ax, ay = min(coords[i], coords[j])
            bx, by = max(coords[i], coords[j])

            a_lower_than_br = ax < brx and ay < bry
            b_higher_than_tl = bx > tlx and by > tly

            if a_lower_than_br and b_higher_than_tl:
                ans = None
                break

    print(ans)

if __name__ == '__main__':
    main()