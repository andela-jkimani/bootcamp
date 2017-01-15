import unittest


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


class TestMethod(unittest.TestCase):

    def test_prime(self):
        self.assertEqual(prime(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(prime(6), [2, 3, 5])

    def test_notPrime(self):
        self.assertTrue(prime(1), 'No prime numbers')
        self.assertTrue(prime(0), 'No prime numbers')

if __name__ == '__main__':
    unittest.main()
