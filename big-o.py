# Big O notation is used to measure how long an algorithm takes to run.
# It allows us to compare the efficiencies of different approaches to a problem.
# Measurement basis: "How quickly runtime grows relative to the input as the input gets larger (usually randomly)"

"""
For the following example, n could be the actual input, or the size of the input.
So n could be an actual number, and it could be the number of items in an input list or map, or object, etc...
"""

# O(1) -> constant time complexity
def constant_big_o(n):
    print(n[0])


# O(n) -> linear time complexity
def linear_big_o(n):
    for item in n:
        print(item)


# O(n^2) -> quadratic time complexity
def quadratic_big_o(n):
    for i in n:
        for j in n:
            print(i, j)


# O(2^n) -> exponential time complexity (e.g. Fibonacci numbers)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


# O(log n) -> Logarithmic time complexity (e.g. Binary Search)
def logarithmic_big_o(n):
    i = 1
    while i <= len(n):
        i = i * 2
