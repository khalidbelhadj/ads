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
def partition(A: list[int], p: int, r: int) -> int:
    return -1

def quick_sort_helper(A: list[int], p: int, r: int, partition: Partition):
    pass

def quick_sort(A: list[int], partition: Partition = partition):
    pass


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
