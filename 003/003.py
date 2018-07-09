import math


def prob003():
    n = 600851475143
    factors = []
    while (n % 2) == 0:
        factors.append(2)
        n = int(n / 2)
    if n > 2:
        factor = 3
        while factor <= math.sqrt(n):
            if (n % factor) == 0:
                factors.append(factor)
                n = int(n / factor)
            else:
                factor += 2
        factors.append(n)
    return factors[-1]


if __name__ == '__main__':
    print(prob003())
