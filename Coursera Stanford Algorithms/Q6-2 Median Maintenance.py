import heapq
#from random import randrange
# TEST DATA
#data = [randrange(-100, 100) for i in range(5)]


def lists():
    """Median maintenance with list implementation - SLOW"""
    medians = []
    for i, n in enumerate(data):
        # check on which position is median
        if i % 2:
            median = i//2
        else:
            median = (i+1)//2
        median = sorted(data[:i+1])[median]
        medians.append(median)
        # print(data[:i+1], 'M:', median)
    return medians


def heaps():
    """Median maintenance with heaps implementation - FASTER"""
    small = []
    big = []
    medians = []
    for i, n in enumerate(data):
        heapq.heappush(big, n)

        # if too many numbers in right heap, insert one to the left heap
        if len(big) > len(small) + 1:
            smaller = heapq.heappop(big)
            heapq.heappush(small, -smaller)

        # if left heap has bigger numbers than right, switch numbers
        if small and -small[0] > big[0]:
            smaller = heapq.heappop(big)
            bigger = heapq.heappushpop(small, -smaller)
            heapq.heappush(big, -bigger)

        # use low heap for odd numbers and high heap for even
        if i % 2:
            median = -small[0]
        else:
            median = big[0]

        medians.append(median)
        # print(small, big, median)
    return medians

if __name__ == '__main__':
    data = []
    with open('data/Q6-2 test1.txt') as file:
        for row in file:
            data.append(int(row))
    print('Analysing data:')
    print(data[:20], '...')
    print('List length:', len(data))
    print()

    # medians_list = lists()
    # print('Medians computed with lists:', medians_list)

    medians = heaps()
    print('Medians computed with heaps:', medians[:100], '...')
    total_sum = sum(medians)
    ans = total_sum % 10000

    print()
    print('SUM:', total_sum)
    print('ANS:', ans)


