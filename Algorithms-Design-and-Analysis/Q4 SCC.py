"""
Algorithms: Design and Analysis, Stanford University for Cousera
Programming Question 4
Find five largest strongly connected components (SCCs) of the graph.
The final file contains directed edges of 875 thousands verticies.
Time execution: 18 seconds for 5.5 Million edges (time for reading is the file not included)
"""

import os
from collections import defaultdict
import logging
import time

# PATH FOR DATA FILE
filename = 'data/Q4 test2.txt'

# Change loggin level to DEBUG if you want to see order of removed nodes
logging.basicConfig(format='%(message)s', level=logging.INFO)


def get_child(parent, graph):
    for child in graph[parent]:
        if child not in visited:
            yield child
    yield False


def dfs(parent):
    visited.add(parent)
    stack.append(parent)
    logging.debug('\nDFS of %s' % parent)

    while stack:
        parent = stack[-1]
        child = next(get_child(parent, Gr))
        if not child:
            parent = stack.pop()
            logging.debug('End for %s' % parent)
            order.append(parent)
            continue
        # logging.info('Analyzing %s' % child)
        stack.append(child)
        visited.add(child)


def dfs2(parent):
    visited.add(parent)
    stack.append(parent)
    size = 1

    while stack:
        parent = stack[-1]
        child = next(get_child(parent, G))
        if not child:
            parent = stack.pop()
            continue
        stack.append(child)
        visited.add(child)
        size += 1
    return size

G = defaultdict(list)
Gr = defaultdict(list)
visited = set()
stack = []
order = []

# Load up file, 13.5s for 5.5 Million edges
with open(filename) as data:
    logging.info('Reading from file... ')
    for row in data:
        key, val = map(int, row.split())
        G[key].append(val)
        Gr[val].append(key)
    logging.info('Finished reading.')

# DFS on reverse graph
for num in sorted(Gr.keys(), reverse = True):
    if num not in visited:
        dfs(num)
logging.info('\n')

visited.clear()
sizes = []

# Find all strong components in the graph and save their size
for num in reversed(order):
    if num not in visited:
        size = dfs2(num)
        sizes.append(size)

# Limit to five biggest groups
ANS = sorted(sizes, reverse = True)[:5]

logging.info('SCC:')
print(*ANS, sep=',')

# Save answer to file
timenow = time.strftime('%H-%S-%S')
name = 'SCC_' + timenow + '.txt'
with open(name, 'w') as data:
    data.write(str(ANS))
    logging.info('Saved to file %s' % name)

input('Done!.')
