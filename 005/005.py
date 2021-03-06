from functools import reduce


def primes_up_to(n):
    """Implementation of the sieve of Eratosthenes"""
    if n < 2:
        return []
    elif n < 3:
        return [2]
    else:
        primes = list(range(3, int(n) + 1, 2))
        oddprimeQs = [True] * ((int(n) - 1) // 2)
        ind = 0
        while primes[ind] ** 2 <= primes[-1]:
            k = primes[ind]
            while primes[ind] * k <= primes[-1]:
                oddprimeQs[(primes[ind] * k - 3)//2] = False
                k += 2
            ind += 1
        return [2] + [p for p in primes if oddprimeQs[(p - 3)//2]]


def prob005():
    """
    All primes up to max must divide the smallest multiple, and so are
    added to the list. For every power of a prime p up to max, we also
    add p again to the list. Now, for every composite number less than
    max, its prime factors were either added to the list in the first
    step (if the prime factor appears only once in the factorization)
    or they were added at least k times to the list in the first and
    second steps, where k is the number of times a given prime appears
    in the factorization.
    """
    max = 20
    factors = primes_up_to(max)
    extrafactors = []
    for f in factors:
        k = 2
        while f ** k <= max:
            extrafactors.append(f)
            k += 1
    return reduce(lambda x, y: x * y, factors + extrafactors)


if __name__ == '__main__':
    print(prob005())
