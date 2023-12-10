import numpy as np
import time
import random


def roots_of_unity(n: int) -> list[complex]:
    return [np.exp(2j * np.pi * k / n) for k in range(n)]


def dft_naive(coeffs: list[complex]) -> list[complex]:
    n = len(coeffs)
    x_values = roots_of_unity(n)
    output = [0 + 0j for _ in range(n)]

    for i in range(len(coeffs)):
        sum = 0
        for j in range(len(coeffs)):
            sum += coeffs[j] * np.power(x_values[i], j)
        output[i] = sum

    return output


def fft(A: list[complex]) -> list[complex]:
    n = len(A)

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
    y = fft(A)
    first = y[0]
    y.reverse()
    y.pop()
    y.insert(0, first)
    return list(map(lambda x: x / len(A), y))


if __name__ == "__main__":
    xs = [random.random() * (100 + 0j) for _ in range(1000)]

    dft_start = time.time()
    dft_value = dft_naive(xs)
    print("DFT naive:", round(time.time() - dft_start, 2))

    fft_start = time.time()
    fft_value = fft(xs)
    print("FFT:", round(time.time() - fft_start, 2))
