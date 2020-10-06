"""
Problem:
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1,2,3,5,8,13,21,34,55,89,..

By considering the terms in the Fibonacci sequence whose values do not exceed
n, find the sum of the even-valued terms. e.g. for n=10, we have {2,8}, sum is
10.
"""


def solution(n: int = 4000000) -> int:
    """Returns the sum of all fibonacci sequence even elements that are lower
    or equals to n.

    >>> solution(10)
    10
    >>> solution(15)
    10
    >>> solution(2)
    2
    >>> solution(1)
    0
    >>> solution(34)
    44
    """
    even_fibs = []
    a, b = 0, 1
    while b <= n:
        if b % 2 == 0:
            even_fibs.append(b)
        a, b = b, a + b
    return sum(even_fibs)


if __name__ == "__main__":
    print(solution(int(input().strip())))
