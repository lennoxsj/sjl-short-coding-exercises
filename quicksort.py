"""Quicksort with median-of-three pivot selection.

Sorts a list and returns the sorted array along with a comparison count.
Median-of-three pivot reduces worst-case behavior on already-sorted or
reverse-sorted inputs.
"""


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def median_of_three(array, left, right):
    mid = (left + right) // 2
    a, b, c = array[left], array[mid], array[right]

    if a <= b <= c or c <= b <= a:
        return mid
    elif b <= a <= c or c <= a <= b:
        return left
    else:
        return right


def partition(array, left, right):
    pivot_value = array[left]
    i = left + 1

    for j in range(left + 1, right + 1):
        if array[j] < pivot_value:
            swap(array, i, j)
            i += 1

    swap(array, left, i - 1)
    return i - 1


def quick_sort(array, left=0, right=None, counter=0):
    if right is None:
        right = len(array) - 1

    if left < right:
        pivot_position = median_of_three(array, left, right)
        swap(array, left, pivot_position)

        p = partition(array, left, right)
        counter += right - left

        array, counter = quick_sort(array, left, p - 1, counter)
        array, counter = quick_sort(array, p + 1, right, counter)

    return array, counter


if __name__ == "__main__":
    example = [50, 3, 587, 92, 1012, 3, 48]
    sorted_array, comparisons = quick_sort(list(example))
    print(f"Original: {example}")
    print(f"Sorted:   {sorted_array}")
    print(f"Comparisons: {comparisons}")
