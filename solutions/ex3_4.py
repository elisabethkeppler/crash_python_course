def primes_search(n):
    """
    Function: 
    Uses the 'Sieve of Erathosthenes' algorithm to find primes less than input value.

    Parameters:
    n  : int        (integer up to which to search for prime numbers)

    Returns:
    list            (a list of the prime numbers less than input value)
    """
    A = [True]* (n+1)
    A[0] = A[1] = False

    for i in range(2, int(n/2+1)):
        if A[i]:
            for j in range(i*i, n+1, i):
                A[j] = False
    
    primes = [i for i, primes_search in enumerate(A) if primes_search]
    return primes

if __name__ == '__main__':
    n = int((input("Insert n up to which to search prime numbers:")))
    print(f"List of prime numbers: {primes_search(n)}")