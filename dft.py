import math


def roots_of_unity(n: int) -> list[complex]:
    """Returns the nth roots of unity"""
    return [math.e ** (2j * math.pi * k / n) for k in range(n)]


def dft_naive(A: list[complex]) -> list[complex]:
    """Naive implementation of DFT"""
    n = len(A)
    if abs(math.frexp(n)[0]) != 0.5:
        raise ValueError("Number of samples must be an integer power of 2.")

    roots = roots_of_unity(n)
    output = [0 + 0j for _ in range(n)]

    for i in range(n):
        sum = 0
        p = 1
        for j in range(n):
            sum += A[j] * p
            p *= roots[i]
        output[i] = sum

    return output


def fft(A: list[complex]) -> list[complex]:
    """Returns the DFT of A using the Fast Fourier Tranform algorithm"""
    n = len(A)
    if abs(math.frexp(n)[0]) != 0.5:
        raise ValueError("Number of samples must be an integer power of 2.")

    if n == 1:
        return A

    roots = roots_of_unity(n)

    A_even = [A[i] for i in range(0, len(A), 2)]
    A_odd = [A[i] for i in range(1, len(A), 2)]

    y_even = fft(A_even)
    y_odd = fft(A_odd)

    y = [0 + 0j for _ in range(n)]

    for k in range(n // 2):
        y[k] = y_even[k] + roots[k] * y_odd[k]
        y[k + n // 2] = y_even[k] - roots[k] * y_odd[k]

    return y


def inverse_fft(A: list[complex]) -> list[complex]:
    """Returns the Inverse DFT of A using the Fast Fourier Tranform algorithm"""
    n = len(A)
    if abs(math.frexp(n)[0]) != 0.5:
        raise ValueError("Number of samples must be an integer power of 2.")

    y = fft(A)
    y.reverse()
    y.insert(0, y.pop())
    return [x / n for x in y]
