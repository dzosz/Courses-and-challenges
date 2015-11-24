"""
The program finds in data pairs of numbers
that sum to anything in [-10000, 10000].
Only one pair per sum.
Returns the number of pairs.
"""
from collections import deque
import bisect


def search_from_sides(data):
    """
    This function uses looks for pairs by slicing the list
    from the sides (the smallest and the biggest).
    """
    def search(i):
        """Searching from the left side of sorted array"""
        count = 0
        for j in deck:
            if j > top:
                # numbers are getting too big
                return count
            elif j >= bottom:
                if i+j not in sums:
                    count += 1
                    sums.add(i+j)
        return count
    def search_rev(i):
        """Searching from the right side - big numbers first"""
        count = 0
        for j in reversed(deck):
            if j < bottom:
                # numbers are getting too small
                return count
            elif j <= top:
                if i+j not in sums:
                    count += 1
                    sums.add(i+j)
        return count

    count = 0
    sums = set()
    deck = deque(data)
    print('Max:', deck[0], 'Min:', deck[-1])
    while deck:
        # Find the biggest absolute number
        if abs(deck[0]) > abs(deck[-1]):
            # Popping the smallest
            i = deck.popleft()
            bottom = -10000 - i
            top = 10000 - i
            # Start looking from the biggest numbers
            count += search_rev(i)
        else:
            # Popping the biggest number
            i = deck.pop()
            bottom = -10000 - i
            top = 10000 - i
            # Lookup from the smallest numbers
            count += search(i)
    return count

def search_binary(data):
    """
    Uses bisect module to locate indices of elementers
    that are within specified range
    """
    count = 0
    sums = set()

    for num in data:
        left = bisect.bisect_left(data, -10000 - num)
        right = bisect.bisect_right(data, 10000 - num)
        for a in range(left, right):
            if num+data[a] not in sums and num != data[a]:
                # print(num, data[a])
                sums.add(num+data[a])
                count+= 1
    return count

if __name__ == '__main__':
    with open('data/Q6-1 test6.txt') as file:
    # with open('data/test5_pa6.txt') as file:
        data = {int(row) for row in file}
    data = sorted(data)
    # data = [-10050, 500, 300, 10005]
    print('file loaded')
    # pairs = search_binary(data)
    pairs = search_from_sides(data)
    print('TOTAL PAIRS:', pairs)
