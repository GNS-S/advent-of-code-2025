from heapq import heappop
from part1 import distance_heap, parse_input

def main():
    boxes = parse_input()

    connections = distance_heap(boxes)
    
    chains: list[set] = [{i} for i in range(len(boxes))]
    last_linked: tuple[int] = None
    while len(chains) != 1:
        _, i, j = heappop(connections)
        last_linked = (i, j)
        current_chain = set([i, j])
        unlinked_chains = []

        for chain in chains:
            if i in chain or j in chain:
                current_chain.update(chain)
            else:
                unlinked_chains.append(chain)

        chains = unlinked_chains + [current_chain]

    i, j = last_linked 
    (ix, _, _), (jx, _, _) = boxes[i], boxes[j]

    print(ix * jx)

if __name__ == '__main__':
    main()