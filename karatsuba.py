"""Karatsuba's algorithm for fast integer multiplication.

Splits each n-digit number into two halves and computes the product with
three recursive sub-multiplications instead of four, giving O(n^log2(3))
≈ O(n^1.585) instead of the schoolbook O(n^2).

Python's built-in `*` already handles big integers efficiently — this is
for understanding the divide-and-conquer pattern, not for performance.
"""


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    a, b = divmod(x, 10 ** half)
    c, d = divmod(y, 10 ** half)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * 10 ** (2 * half) + ad_plus_bc * 10 ** half + bd


if __name__ == "__main__":
    x = 1234567891234567
    y = 9876543219876543

    result = karatsuba(x, y)
    expected = x * y

    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Karatsuba: {result}")
    print(f"Built-in:  {expected}")
    print(f"Match:     {result == expected}")
