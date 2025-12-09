from heapq import heappop, heappush
from itertools import pairwise, combinations
from part1 import parse_input, rectangle_area

def main():
    coords = parse_input()

    area_heap = []

    for a, b in combinations(coords, 2):
        x1, y1 = a
        x2, y2 = b
        
        topleft = min(x1, x2), min(y1, y2)
        botright = max(x1, x2), max(y1, y2)
        area = rectangle_area(a, b)

        heappush(area_heap, (-area, topleft, botright))

    normalized_edges = []
    for a, b in pairwise(coords + [coords[0]]):
        normalized_edges.append((min(a, b), max(a, b)))

    ans = None
    while area_heap and ans == None:
        negative_area, topleft, botright = heappop(area_heap)
        tlx, tly = topleft
        brx, bry = botright
        midpointx, midpointy = (brx + tlx + 1) / 2, (bry + tly + 1) / 2

        ans = -negative_area

        is_inside_polygon = False
        for a, b in normalized_edges:
            ax, ay = a
            bx, by = b

            a_lower_than_br = ax < brx and ay < bry
            b_higher_than_tl = bx > tlx and by > tly

            if a_lower_than_br and b_higher_than_tl:
                ans = None
                break

            # https://en.wikipedia.org/wiki/Even-odd_rule
            # Ray-cast to the right of the midpoint and count edges to determine insidedness.
            # Prevents edge cases where the rectangle is outside the polyhedron with no intersection
            if ax == bx and ax > midpointx and ay <= midpointy < by:
                is_inside_polygon = not is_inside_polygon

        if not is_inside_polygon:
            ans = None

    print(ans)

if __name__ == '__main__':
    main()