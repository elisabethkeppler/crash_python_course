def div_test(a, b):
    """
    Function: 
    Checks if a is divisible by b.

    Parameters:
    a  : int
    b  : int

    Returns:
    bool            (True if a is divisible by b, False otherwise)
    """
    return a % b == 0

def div_check(n):
    """
    Function:
    Prints which of [2, 3, 5, 7] divide a given input value.

    Parameters:
    n : int

    Returns:
    [2, 3, 5, 7]
    """
    for d in [2,3,5,7]:
        if div_test(n, d):
            print(f"{n} is divisible by {d}")

if __name__ == '__main__':
    a = int((input("First integer to be checked: ")))
    b = int((input("Second integer to be checked: ")))

    print()
    div_check(a)
    
    print()
    print(f"{a} is {'' if div_test(a,b) else 'not'} by {b}")
    print(f"{b} is {'' if div_test(b,a) else 'not'} by {a}")
