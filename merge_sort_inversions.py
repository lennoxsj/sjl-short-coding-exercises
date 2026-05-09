"""Merge sort that also counts inversions.

An inversion is a pair (i, j) where i < j but arr[i] > arr[j] — a measure
of how out-of-order a list is. Counting inversions naively is O(n^2);
merge sort gets it for free in O(n log n) by tallying how many left-side
elements remain each time a right-side element is taken during merging.
"""


def merge(left, right):
    merged = []
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions


def merge_sort(array):
    if len(array) <= 1:
        return array, 0

    mid = len(array) // 2
    left, left_inv = merge_sort(array[:mid])
    right, right_inv = merge_sort(array[mid:])
    merged, split_inv = merge(left, right)

    return merged, left_inv + right_inv + split_inv


if __name__ == "__main__":
    example = [50, 3, 587, 92, 1012, 3, 48]
    sorted_array, inversions = merge_sort(example)
    print(f"Original:   {example}")
    print(f"Sorted:     {sorted_array}")
    print(f"Inversions: {inversions}")
