"""
real    0m1.142s

Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the
terms increases by 3330, is unusual in two ways: (i) each of the
three terms are prime, and, (ii) each of the 4-digit numbers are
permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-,
or 3-digit primes, exhibiting this property, but there is one
other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms
in this sequence?
"""

from itertools import combinations, permutations, combinations_with_replacement


def is_prime(number):
    divisors = 0
    start_num = 2
    for i in range(2, number//2+1):
        if not number % i:
            divisors += 1
            if divisors > 1:
                return False
    return True


digits = list(map(str, range(0,10)))
possibles = combinations_with_replacement(digits, 4)

for number in possibles:
    primes = []
    for num in permutations(number):
        # discard three digit numbers
        if num[0] == '0':
            continue
        num = int(''.join(num))
        if is_prime(num):
            primes.append(num)
    if len(primes) > 2:
        # check all the prime triplets in combination
        for a, b, c in combinations(primes, 3):
            if a+3330 == b == c - 3330:
                print(a, b, c)
                break
