import numpy as np

def roots_of_unity(n: int) -> list[complex]:
    return [np.exp(2j * np.pi * k / n) for k in range(n)]

def dft_naive(coeffs: list[float]) -> list[complex]:
    x_values = roots_of_unity(len(coeffs))
    output = [0 + 0j] * len(x_values)

    for i in range(len(x_values)):
        sum = 0
        for j in range(len(coeffs)):
            sum += (coeffs[j] * i) ** j
        output[i] = sum

    return output

def fft(A: list[float]) -> list[complex]:
    raise NotImplementedError


def inverse_fft(B: list[float]) -> list[complex]:
    raise NotImplementedError


if __name__ == '__main__':
    print(fft([1, 2, 3]))