# scoping stuff withr recursion


def fact(n):
    """ Calculate factorial of n, n!. """

    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


# function calls itself for factorial(n-1) repeatedly until can return factorial(n)
def factorial(n):
    """ Calculates n! recursively, n! = n * (n-1)!. """

    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    """ Calculate fibonacci sequence f(n) = f(n-1) + f(n-2). """

    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    """ Faster without recursion. """

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus_1 = 1
        n_minus_2 = 0
        for f in range(1, n):
            result = n_minus_2 + n_minus_1
            n_minus_2 = n_minus_1
            n_minus_1 = result
    return result


for i in range(36):
    print(i, fib(i), "\t", fibonacci(i))
