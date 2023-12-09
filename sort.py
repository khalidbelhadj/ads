from random import randint
from typing import Callable


# Insert Sort -----------------------------------
def insert_sort(A: list[int]):
    if len(A) <= 1:
        return

    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and x <= A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = x


# Merge Sort ------------------------------------
def merge(A: list[int], merge_range: tuple[int, int, int]):
    B: list[int] = []

    (p, q, r) = merge_range
    i, j = (p, q + 1)

    while i <= q or j <= r:
        if j > r or (i <= q and (A[i] <= A[j])):
            # take from the left
            # - when the right is out of stuff
            # - when the left is smaller than the right
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    A[p:r + 1] = B


def merge_sort_helper(A: list[int], sort_range: tuple[int, int]):
    range_length = sort_range[1] - sort_range[0] + 1

    if range_length <= 1:
        return
    else:
        p = sort_range[0]
        q = sort_range[0] + range_length // 2 - 1
        r = sort_range[1]

        merge_sort_helper(A, (p, q))
        merge_sort_helper(A, (q + 1, r))
        merge(A, (p, q, r))


def merge_sort(A: list[int]):
    merge_sort_helper(A, (0, len(A) - 1))


Partition = Callable[[list[int], int, int], int]


# Quick Sort ------------------------------------
def median_of_3_partition(A: list[int], p: int, r: int) -> int:
    xs = sorted([A[p], A[(p + r) // 2], A[r - 1]])
    return xs[1]


def quick_sort_helper(A: list[int], p: int, r: int, partition_fn: Partition):
    if r - p <= 1:
        return

    pivot = A.pop(partition_fn(A, p, r))

    # i holds the index of the last element that is greater than the pivot value
    i = p

    for j in range(p, r - 1):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A.insert(i, pivot)

    quick_sort_helper(A, p, i, partition_fn)
    quick_sort_helper(A, i, r, partition_fn)

def quick_sort(A: list[int], partition_fn: Partition = median_of_3_partition):
    quick_sort_helper(A, 0, len(A), partition_fn)


# Non-comparative sorting -----------------------
def counting_sort(A, m, key_fn=lambda x: x):
    n = len(A)
    C = [0] * m

    # C[i] is the number of elements in A that are == i
    for _, key in enumerate(A):
        C[key_fn(key)] += 1

    # C[i] is now the number of elements in A that are >= i
    for i in range(1, m):
        C[i] += C[i - 1]

    B = [None] * n

    for i in range(n - 1, -1, -1):
        j = A[i]
        B[C[key_fn(j)] - 1] = A[i]
        C[key_fn(j)] -= 1

    A[:] = B

def digit_at(n: int, i: int) -> int:
    return int(str(n)[i]) if i < len(str(n)) else 0

def radix_sort(A: list[int]):
    max_digits = max(map(lambda x: len(str(x)), A))

    for i in range(max_digits - 1, -1, -1):
        counting_sort(A, 10, key_fn=lambda x : digit_at(x, i))

# Testing ---------------------------------------
def quick_test(list_length: int, *args: Callable[[list[int]], None]):
    lists: list[list[int]] = []
    A: list[int] = []

    for _ in range(list_length):
        A.append(randint(0, 1000))
    for f in args:
        B = A[:]
        f(B)
        lists.append(B)
    return all(map(lambda x: x[0] == x[1], list(zip(lists, lists[1:]))))


def main():
    A = [112, 495, 971, 135, 200, 111, 500]
    radix_sort(A)
    print(A)


if __name__ == '__main__':
    main()
