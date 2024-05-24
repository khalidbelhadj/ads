from typing import Callable


def insert_sort(A: list[float]):
    """Sorts the list A using insert sort in place"""
    if len(A) <= 1:
        return

    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] >= key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def merge(A: list[float], p: int, q: int, r: int):
    B: list[float] = []
    i, j = (p, q)

    while i < q or j < r:
        if j >= r or (i < q and (A[i] <= A[j])):
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    A[p:r] = B


def merge_sort(A: list[float], p: int, r: int):
    """Sorts the list A using merge sort within sort_range"""
    if r - p <= 1:
        return

    q = (p + r) // 2

    merge_sort(A, p, q)
    merge_sort(A, q, r)
    merge(A, p, q, r)


"""Type variable of function which returns the index of the pivot"""
PivotFn = Callable[[list[float], int, int], int]


def partition(A: list[float], p: int, r: int, pivot_fn: PivotFn) -> int:
    pivot_idx = pivot_fn(A, p, r)
    A[pivot_idx], A[r - 1] = A[r - 1], A[pivot_idx]

    pivot = A[r - 1]
    i = p

    for j in range(p, r - 1):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r - 1] = A[r - 1], A[i]
    return i


def quicksort(
    A: list[float], p: int, r: int, pivot_fn: PivotFn = lambda _, p, r: r - 1
):
    """Sorts the list A using quicksort within the range p..r"""
    if r - p <= 1:
        return

    q = partition(A, p, r, pivot_fn)
    quicksort(A, p, q, pivot_fn)
    quicksort(A, q, r, pivot_fn)


KeyFn = Callable[[int], int]


def counting_sort(A: list[int], m: int, key_fn: KeyFn = lambda x: x):
    """Sorts the list A using counting sort, given that A[i] <= m"""
    if not all(0 <= key_fn(a) < m for a in A):
        raise ValueError(f"Elements of list must be between 0 and {m}")

    n = len(A)
    C = [0] * m

    # C[i] is the number of elements in A that are == i
    for _, i in enumerate(A):
        C[key_fn(i)] += 1

    # C[i] is now the number of elements in A that are <= i
    for i in range(1, m):
        C[i] += C[i - 1]

    B: list[int] = [0] * n

    for i in range(n - 1, -1, -1):
        j: int = key_fn(A[i])
        C[j] -= 1
        B[C[j]] = A[i]

    A[:] = B


def get_digit(n: int, i: int) -> int:
    """Returns the ith digit of n. Returns 0 if i is greater than the number of digits"""
    s = str(n)
    if i >= len(s):
        return 0

    return int(s[-(i + 1)])


def radix_sort(A: list[int]):
    """Sorts the list A using radix sort, given that 0 < A[i] <= m"""
    # Largest number of digits
    d = len(str(max(A)))

    for i in range(d):
        counting_sort(A, 10, lambda x: get_digit(x, i))
