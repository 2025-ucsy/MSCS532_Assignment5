"""
Benchmark deterministic vs. randomized Quicksort vs. Mergesort
on random, sorted, and reverse‑sorted arrays.

Also prints a succinct demonstration to feed into output.txt.
"""

from __future__ import annotations
import random, time, sys
from typing import List

from quicksort import quicksort
from quicksort_randomized import quicksort_randomized


# ----------- simple mergesort for comparison --------------------------
def mergesort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = mergesort(arr[:mid]), mergesort(arr[mid:])
    merged: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged
# ----------------------------------------------------------------------


def _time_it(func, data: List[int]) -> float:
    copied = data.copy()
    start = time.perf_counter()
    if func is mergesort:
        _ = func(copied)
    else:
        func(copied)
    return time.perf_counter() - start


def benchmark() -> None:
    sizes = [1_000, 5_000, 10_000]
    algs = [
        ("Det Quick", quicksort),
        ("Rand Quick", quicksort_randomized),
        ("Merge", mergesort),
    ]

    dist_builders = {
        "Random": lambda n: [random.randint(0, 10_000) for _ in range(n)],
        "Sorted": lambda n: list(range(n)),
        "Reverse": lambda n: list(range(n, 0, -1)),
    }

    for dist_name, make_data in dist_builders.items():
        print(f"\n=== {dist_name} arrays ===")
        for n in sizes:
            data = make_data(n)
            results = " | ".join(
                f"{name}: { _time_it(fn, data):5.4f}s" for name, fn in algs
            )
            print(f"n={n:>6}: {results}")


if __name__ == "__main__":
    print("Empirical Timing Benchmark")
    benchmark()
