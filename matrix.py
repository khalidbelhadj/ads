import math
import numpy as np

matrix = np.matrix[float, np.dtype[np.float64]]


def matmul_naive(A: matrix, B: matrix) -> matrix:
    """Naive implementation of matrix multiplication"""
    if A.shape[1] != B.shape[0]:
        raise ValueError(f"Invalid dimensions of matrices: {A.shape} x {B.shape} ")

    n, m = A.shape
    output = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            product = 0
            for k in range(n):
                product += A[i, k] * B[k, j]
            output[i, j] = product

    return matrix(output)


def matmul_dnc(A: matrix, B: matrix) -> matrix:
    """Multiplies matrices A and B using the conquer method"""
    n, m = A.shape

    if n != m:
        raise Exception("Matrices must be square")

    if A.shape != B.shape:
        raise ValueError("Matrices must have the same shape")

    if n == 1:
        return matmul_naive(A, B)

    a11, a12, a21, a22 = (
        A[: n // 2, : n // 2],
        A[: n // 2, n // 2 :],
        A[n // 2 :, : n // 2],
        A[n // 2 :, n // 2 :],
    )
    b11, b12, b21, b22 = (
        B[: n // 2, : n // 2],
        B[: n // 2, n // 2 :],
        B[n // 2 :, : n // 2],
        B[n // 2 :, n // 2 :],
    )

    C11 = matmul_dnc(a11, b11) + matmul_dnc(a12, b21)
    C12 = matmul_dnc(a11, b12) + matmul_dnc(a12, b22)
    C21 = matmul_dnc(a21, b11) + matmul_dnc(a22, b21)
    C22 = matmul_dnc(a21, b12) + matmul_dnc(a22, b22)

    return matrix(np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22)))))


def matmul_strassen(A: matrix, B: matrix) -> matrix:
    """Multiplies matrices A and B using Strassen's algorithm"""
    n, m = A.shape

    if n != m:
        raise Exception("Matrices must be square")

    if A.shape != B.shape:
        raise ValueError("Matrices must have the same shape")

    if n == 1:
        return matmul_naive(A, B)

    # When n is not a power of 2, pad to the closest power of 2
    if abs(math.frexp(n)[0]) != 0.5:
        padding = 2 ** math.ceil(math.log2(n)) - n
        return matmul_strassen(
            matrix(np.pad(A, ((0, padding), (0, padding)), "empty")),
            matrix(np.pad(B, ((0, padding), (0, padding)), "empty")),
        )[:n, :n]

    half = n // 2
    a11, a12, a21, a22 = (
        A[:half, :half],
        A[:half, half:],
        A[half:, :half],
        A[half:, half:],
    )

    b11, b12, b21, b22 = (
        B[:half, :half],
        B[:half, half:],
        B[half:, :half],
        B[half:, half:],
    )

    P1 = matmul_strassen(matrix(a11 + a22), matrix(b11 + b22))
    P2 = matmul_strassen(matrix(a21 + a22), b11)
    P3 = matmul_strassen(a11, matrix(b12 - b22))
    P4 = matmul_strassen(a22, matrix(-b11 + b21))
    P5 = matmul_strassen(matrix(a11 + a12), b22)
    P6 = matmul_strassen(matrix(-a11 + a21), matrix(b11 + b12))
    P7 = matmul_strassen(matrix(a12 - a22), matrix(b21 + b22))

    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 + P3 - P2 + P6

    return matrix(np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22)))))


def maxtrix_chain_order(A: list[int]):
    """Computes the optimal order for matrix multiplcation"""
    m = np.zeros((len(A), len(A)))
    s = np.zeros((len(A), len(A)))

    for subseq_len in range(2, len(A)):
        for i in range(0, len(A) - subseq_len):
            j = i + subseq_len
            m[i, j] = float("inf")
            for k in range(i + 1, j):
                q = m[i, k] + m[k, j] + A[i] * A[k] * A[j]
                if q < m[i, j]:
                    m[i, j] = q
                    s[i, j] = k
    return s, m
