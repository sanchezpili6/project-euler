"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def even_fibonacci():
    previous_n = 0
    n = 1
    even_valued_sum = 0
    while n <= 4000000:
        temp = n
        n += previous_n
        previous_n = temp
        if n % 2 == 0:
            even_valued_sum += n
    return even_valued_sum


print(even_fibonacci())