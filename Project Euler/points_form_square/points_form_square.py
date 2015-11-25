import math

ans = True
p1 = (-1, 0)
p2 = (0, 1)
p3 = (1, 0)
p4 = (0, -1)
data = [p1, p2, p3, p4]

"""Check if points do not overlap."""
if len(data) != len(set(data)):
    ans = False

distances = set()
for a in data:
    for b in data:
        if a == b:
            continue
        dist = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        distances.add(dist)

# UGLY VERSION
# set(math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2) for a in data for b in data if a!=b)

"""
Check if only two distinct distances exist
and if the longer distance is a diagonal of a square.
Uses approximate equality to compare.
"""
if len(distances) != 2 or abs(1 - max(distances) / math.sqrt(2) / min(distances)) > 0.01:
    ans = False

print(ans)
