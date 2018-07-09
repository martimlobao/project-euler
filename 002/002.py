def prob002():
    fibs = [1, 2]
    while fibs[-1] + fibs[-2] < 4000000:
        fibs.append(fibs[-1] + fibs[-2])
    return sum(even for even in fibs if even % 2 == 0)


if __name__ == '__main__':
    print(prob002())
