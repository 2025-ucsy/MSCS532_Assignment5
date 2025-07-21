"""
Randomized Quicksort: picks a random pivot in every recursive call.

Guarantees expected Θ(n log n) even for adversarial inputs.
"""

from __future__ import annotations
import random
from typing import List


def _partition(arr: List[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


def quicksort_randomized(arr: List[int], lo: int = 0, hi: int | None = None) -> None:
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        # 1‑line random‑pivot swap
        pivot_index = random.randint(lo, hi)
        arr[pivot_index], arr[hi] = arr[hi], arr[pivot_index]

        p = _partition(arr, lo, hi)
        quicksort_randomized(arr, lo, p - 1)
        quicksort_randomized(arr, p + 1, hi)


if __name__ == "__main__":
    arr = [random.randint(0, 99) for _ in range(20)]
    print("Before:", arr)
    quicksort_randomized(arr)
    print("After :", arr)
