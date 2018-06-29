# wrap code in try and except to prevent a crash


def factorial(n):
    """Calculate n! recursively."""

    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(1000))
except (RecursionError, ZeroDivisionError):
    print("[Factorial Error/Zero Division Error]")

print("\nThe program is terminating.")
