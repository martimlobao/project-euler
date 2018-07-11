def prob004():
    prod = set()
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod.add(i * j)
    palin = [n for n in prod if n == int(str(n)[::-1])]
    return max(palin)


if __name__ == '__main__':
    print(prob004())
