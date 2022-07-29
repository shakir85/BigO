# Big O notation is used to measure how long an algorithm takes to run.
# It allows us to compare the efficiencies of different approaches to a problem.
# Measurement basis: "How quickly runtime grows relative to the input as the input gets larger (usually randomly)"

# Time Complexity: >> Time cost of an algorithm to execute a set of instructions (relative to the input?).
# Space Complexity: >> Memory cost of an algorithm to execute a set of instructions. (relative to the input?).
"""
For the following examples, n could be the actual input, or the size of the input.
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


"""
    Drop The Constants!
    Steps of a constant time complexity can be dropped because they have
    no significant effect. Also in big-o we are only interested for the events
    that happen when n gets arbitrarily large.
"""


# throw out the constants, instead of saying O(2n), it's called O(n)
def drop_the_constant_1(n):
    # one occurrence 1
    for i in n:
        print(i)
    # second occurrence 1, so we don't add identical steps like 1 + 1
    for i in n:
        print(i)


# same thing, these are constant time complexity
def drop_the_constant_2(n):
    """
    Instead of saying this function's big-o = O(1 + n/2 + 1000) we drop the constants
    and we just say big-o = O(n)
    """
    # constant complexity O(1)
    print(n[0])

    # This is also a constant complexity O(n/2)
    middle = len(n) // 2
    index = 0
    # This is linear time complexity
    while index <= middle:
        print(n[index])
        index += 1

    # This is also a constant time complexity
    for _ in range(1000):
        print("hi")


"""
    Best-Case, Worst-Case
    In big-o, we typically focus on worst-case step in the algorithm that generates
    more time-complexity. This is the opposite of big-o theta = best case, or big-o omega = average case.
    We also can use a combination of the three to estimate the worst, good, and average cases. 
"""


# best-case O(1) and worst-case would be O(n) for the following function:
def find_the_item(large_bag, item):
    for i in large_bag:
        # best case when the item is at the beginning of the bag = O(1)
        # worst case when it's at the end of the bag = O(n)
        # So generally this worst-case depends on the size of n.
        if i == item:
            return True

    return False

if __name__ == "__main__":
    pass
