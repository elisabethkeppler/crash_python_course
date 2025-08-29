from ex3_1 import div_test
from ex3_4 import primes_search

def prime_factors(n):
    """
    Function:
    Decomposes a positive integer into its prime factors.

    Parameters:
    n : int     (a positive integer >=1 to decompose in prime factors)

    Returns:
    list        (a list of the prime factors of the input value, with repetition)
    """
    if n<2:
        return []
    
    factors = []
    primes = primes_search(n)

    for p in primes:
        while div_test(n,p):
            factors.append(p)
            n //= p
        if n == 1:
            break
    
    return factors

def _test():
    """
    Test:
    Tests the correctness of the prime factor decomposition for the first 100 numbers.
    """
    for n in range(1,101):
        factors = prime_factors(n)
        product = 1
        for f in factors:
            product *= f
        assert product == n, f"Error at n={n}, factors={factors}"
        print(f"{n}= {' * '.join(map(str, factors))}")

if __name__=='__main__':
    n = int((input("Insert number to decompose into prime factors:")))
    print(f"{n} is decomposed in the product between these prime factors: {prime_factors(n)}")
    print()
    _test()