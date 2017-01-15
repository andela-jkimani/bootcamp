def prime(n):
    numbers = []
    for x in range(0, n):
        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:
                    break
            else:
                numbers.append(x)
    print numbers

prime(20)
