"""
Deterministic (last‑element) Quicksort implementation.

Time‑complexity:
  • Best / average:  Θ(n log n)
  • Worst (already‑sorted):  Θ(n²)
Space: O(log n)  due to recursion stack in average case.

Usage:
    python quicksort.py
"""

from __future__ import annotations
from typing import List


def _partition(arr: List[int], lo: int, hi: int) -> int:
    """Partition using last element as pivot; returns final pivot index."""
    pivot = arr[hi]
    i = lo - 1                      # index of smaller element
    for j in range(lo, hi):
        if arr[j] <= pivot:         # stable-ish: ≤ keeps equal keys left
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


def quicksort(arr: List[int], lo: int = 0, hi: int | None = None) -> None:
    """In‑place deterministic Quicksort."""
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = _partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        [], [1], [2, 1], [3, 2, 1],
        [5, 1, 4, 2, 8], [3, 3, 3, 2, 1],
        list(range(10)),             # already sorted (worst‑case)
    ]
    for case in test_cases:
        print("Original :", case)
        quicksort(case)
        print("Sorted   :", case, "\n")
