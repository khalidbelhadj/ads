import numpy as np

Matrix = np.matrix[int, np.dtype[np.int64]]


def mat_add(A: Matrix, B: Matrix) -> Matrix:
    if A.shape != B.shape:
        raise Exception("Matrices must be the same shape")

    output = np.zeros((A.shape[0], A.shape[1]))

    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            output[i, j] = A[i, j] + B[i, j]

    return Matrix(output)


def mat_mult_naive(A: Matrix, B: Matrix) -> Matrix:
    n = A.shape[1]
    m = A.shape[0]

    if n != m:
        raise Exception("Matrices must be square")

    output = np.zeros((A.shape[0], B.shape[1]))

    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            product = 0
            for k in range(n):
                product += A[i, k] * B[k, j]
            output[i, j] = product

    return Matrix(output)


def mat_mult_dnc(A: Matrix, B: Matrix) -> Matrix:
    n = A.shape[1]
    m = A.shape[0]

    if n != m:
        raise Exception("Matrices must be square")

    if n == 1:
        return mat_mult_naive(A, B)

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

    C11 = mat_add(mat_mult_dnc(a11, b11), mat_mult_dnc(a12, b21))
    C12 = mat_add(mat_mult_dnc(a11, b12), mat_mult_dnc(a12, b22))
    C21 = mat_add(mat_mult_dnc(a21, b11), mat_mult_dnc(a22, b21))
    C22 = mat_add(mat_mult_dnc(a21, b12), mat_mult_dnc(a22, b22))

    return Matrix(np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22)))))


def mat_mult_strassen(A: Matrix, B: Matrix) -> Matrix:
    n = A.shape[1]
    m = A.shape[0]

    if n != m:
        raise Exception("Matrices must be square")

    if n == 1:
        return mat_mult_naive(A, B)

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

    P1 = mat_mult_strassen(a11, mat_add(b12, -Matrix(b22)))
    P2 = mat_mult_strassen(mat_add(a11, a12), b22)
    P3 = mat_mult_strassen(mat_add(a21, a22), b11)
    P4 = mat_mult_strassen(a22, mat_add(b21, -Matrix(b11)))
    P5 = mat_mult_strassen(mat_add(a11, a22), mat_add(b11, b22))
    P6 = mat_mult_strassen(mat_add(a12, -Matrix(a22)), mat_add(b21, b22))
    P7 = mat_mult_strassen(mat_add(a11, -Matrix(a21)), mat_add(b11, b12))

    C11 = mat_add(mat_add(P5, P4), mat_add(-Matrix(P2), P6))
    C12 = mat_add(P1, P2)
    C21 = mat_add(P3, P4)
    C22 = mat_add(mat_add(P5, P1), mat_add(-Matrix(P3), -Matrix(P7)))

    return Matrix(np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22)))))


def maxtrix_chain_mult(A: list[int]):
    m = np.zeros((len(A), len(A)))
    s = np.zeros((len(A), len(A)))

    for subseq_len in range(2, len(A)):
        for i in range(0, len(A) - subseq_len):
            j = i + subseq_len
            m[i, j] = float("inf")
            for k in range(i + 1, j):
                # q = cost of split 1 + cost of split 2 + cost of merge
                q = m[i, k] + m[k, j] + A[i] * A[k] * A[j]
                if q < m[i, j]:
                    m[i, j] = q
                    s[i, j] = k
    return s, m


def main():
    s, m = maxtrix_chain_mult([30, 1, 40, 10, 25])
    for a in s:
        print(a)

    for a in m:
        print(a)

    # type: ignore
    # print(
    #     mat_mult_naive(np.matrix([[1, 2], [3, 4]]),
    #                    np.matrix([[1, 2], [3, 4]])))
    # print(
    #     mat_mult_dnc(np.matrix([[1, 2], [3, 4]]),
    #                  np.matrix([[1, 2], [3, 4]])))
    # print(
    #     mat_mult_strassen(np.matrix([[1, 2], [3, 4]]),
    #                       np.matrix([[1, 2], [3, 4]])))


if __name__ == "__main__":
    main()
