"""
The program uses dijkstra algorithm to find the shortest path to
specified verticies in the graph.
Returns minimum cost.
"""
from collections import defaultdict
import heapq
import copy


def dijkstra_cost(goals, options):
    """
    Pass list of goals in argument and starting information.
    Yields costs for encountered goals.
    """
    cost, pos, path = options[0]
    visited = set()
    while goals:
        # check if reached any specific goal
        if pos in goals:
            goals.remove(pos)
            yield pos, cost

        # if no any other connections - skip
        if not options:
            continue

        # get the least expensive option
        cost, pos, path = heapq.heappop(options)
        if pos not in visited:
            visited.add(pos)
        else:
            continue

        # add each child-edge to options with specific cost
        for to, c in G[pos]:
            if to not in visited:
                heapq.heappush(options, (c+cost, to, path+[to]))
    return False

if __name__ == '__main__':
    # load nodes to dictionaries
    with open('data/Q5 test7.txt') as f:
        G = defaultdict(list)
        for row in f:
            parent, *pairs = row.split()
            parent = int(parent)
            for pair in pairs:
                child, cost = map(int, pair.split(','))
                G[parent].append((child, cost))
                G[child].append((parent, cost))
        print('File loaded.')

    # GENERAL SETTINGS FOR SEARCHING
    start = 1
    options = [(0, start, [])]
    costs = {}
    find_path_for = [5, 10, 15, 34]
    # find_path_for = list(G.keys())

    print('The minimum costs are:')
    # loop over function that yields finished goals
    for node, cost in dijkstra_cost(find_path_for, copy.copy(options)):
        costs[node] = cost
        print('Node:', node, '-->', cost, end='\n')

    print('')
    print('Paths:', costs.keys())
    print('Costs:', costs.values())
