def fibonacci(n):
    """
    Function: 
    Calculates the Fibonacci sequence up to the n-th term.

    Parameters:
    n  : int        (the number of elements of the Fibonacci sequence to be returned)

    Returns:
    list            (a list with the Fibonacci sequence up to the n-th term)
    """
    if n<=0:
        return []
    
    fibseq = [0,1]
    for _ in range(2,n):
        fibseq.append(fibseq[-1]+fibseq[-2])
    return fibseq[:n]

def _test1(n):
    """
    Test 1:
    Generates the Fibonacci sequence using a while-loop and stores the elements in a list.

    Parameters:
    n : int     (the number of elements of the Fibonacci sequence to be returned)

    Returns:
    list            (a list with the Fibonacci sequence up to the n-th term)
    """
    print("Test 1: while-loop")
    fib_list = []

    a, b = 0, 1
    count = 0

    while count < n:
        fib_list.append(a)
        a, b = b, a + b
        count += 1

    return fib_list
    
def _test2(n):
    """
    Test 2:
    Generates the Fibonacci sequence using a for-loop and stores the elements
    in a dictonary with the index as the key.

    Parameters:
    n : int     (the number of elements of the Fibonacci sequence to be returned)

    Returns:
    list            (a list with the Fibonacci sequence up to the n-th term)
    """
    print("Test 2: for-loop with dictionary")
    fib_dict = {}

    for i in range(n):
        if i == 0:
            fib_dict[i] = 0
        elif i == 1:
            fib_dict[i] = 1
        else:
            fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]

    return list(fib_dict.values())

if __name__ == '__main__':
    n = int((input("Insert n to calculate the n-th element of the Fibonacci sequence:")))
    print(f"main Fibonacci sequence implementation: {fibonacci(n)}")
    print(f"while-loop test result: {_test1(n)}")
    print("for-loop with dictionary test result: ", _test2(n))
