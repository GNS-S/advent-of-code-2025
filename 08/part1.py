from os import path
from math import sqrt, prod
from heapq import heappop, heappush

INPUT_DIR = path.dirname(path.realpath(__file__))
INPUT_PATH = f'{INPUT_DIR}/input.txt'

def main():
    boxes = parse_input()

    connection_count = 1000
    connections = distance_heap(boxes)

    chains: list[set] = []
    for _ in range(connection_count):
        _, i, j = heappop(connections)
        current_chain = set([i, j])
        unlinked_chains = []

        for chain in chains:
            if i in chain or j in chain:
                current_chain.update(chain)
            else:
                unlinked_chains.append(chain)
        
        chains = unlinked_chains + [current_chain]
    
    lengths = sorted([len(chain) for chain in chains])
    print(prod(lengths[-3:]))

def parse_input() -> list[tuple[int, int,int]]:
    with open(INPUT_PATH) as f:
        lines = f.read().strip().split('\n')

        boxes = []
        for line in lines:
            x, y, z = line.split(',')
            boxes.append((int(x), int(y), int(z)))

        return boxes
    
def distance_heap(boxes: list[tuple[int, int,int]]) -> list[tuple[int, int,int]]:
    """
    Returns a heap of connection tuples - (distance, box1 index, box2 index)
    """
    connections: list[tuple[int, int,int]] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            x1, y1, z1 = boxes[i]
            x2, y2, z2 = boxes[j]
            distance = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            heappush(connections, (distance, i, j))

    return connections

    
if __name__ == '__main__':
    main()