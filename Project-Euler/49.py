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

nums = list(map(str, range(0,10)))
pairs = combinations_with_replacement(nums, 4)

for number in pairs:
    # check permutations
    primes = []
    for num in permutations(number):
        if num[0] == '0':
            continue
        num = int(''.join(num))
        if is_prime(num):
            primes.append(num)
    if len(primes) > 2:
        for a, b, c in combinations(primes, 3):
            if a+3330 == b == c - 3330:
                print(a, b, c)
                break
