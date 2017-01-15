def prime(n):
    if n > 1:
        numbers = []
        for x in range(0, n):
            if x > 1:
                for i in range(2, x):
                    if (x % i) == 0:
                        break
                else:
                    numbers.append(x)
        return numbers
    else:
        return 'No prime numbers'

print prime(0)
