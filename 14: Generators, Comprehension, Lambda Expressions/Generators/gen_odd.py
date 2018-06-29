def odd():
    """Generate odd numbers."""

    current = 1
    while True:
        yield current
        current += 2


def pi_series():
    """Leibnitz series."""

    odds = odd()
    approx = 0

    while True:
        approx += (4/(next(odds)))
        yield approx  # will stop here in loop then exit
        approx -= (4/(next(odds)))
        yield approx  # then continue from here on next loop


approx_pi = pi_series()

for x in range(100000):
    print(next(approx_pi))
