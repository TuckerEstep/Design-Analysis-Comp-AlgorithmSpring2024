import time
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def pollards_rho_factorization(n):
    if n <= 1:
        return None
    if n % 2 == 0:
        return 2

    x = random.randint(1, n - 1)
    y = x
    d = 1

    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        d = gcd(abs(x - y), n)

    if d == n:
        return None
    return d

def f(x, n):
    return (x ** 2 + 1) % n

def factorize(n):
    factors = []

    if n <= 1:
        return None
    if n % 2 == 0:
        factors.append(2)
        n //= 2
    if n % 3 == 0:
        factors.append(3)
        n //= 3

    while n > 1:
        if is_prime(n):
            factors.append(n)
            break
        factor = pollards_rho_factorization(n)
        if factor is None:
            return None
        factors.append(factor)
        n //= factor
    return factors

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    number_to_factorize = int(input("Enter a number to factorize:"))
    start_time = time.time()
    factors = factorize(number_to_factorize)
    end_time = time.time()
    if factors is not None:
        print(f"Prime factors of {number_to_factorize}: {factors}")
    else:
        print(f"Failed to factorize {number_to_factorize}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
