# Fibonacci Sequence

# Write a recursive function of the form fib(n) that produces the n-th number 
# in the Fibonacci sequence, {0, 1, 1, 2, 3, 5, 8, ...}
from typing import List

def fib(n: int) -> int:
    """
    """
    if n < 2:
        return n
    if n >= 2:
        return fib(n-1) + fib(n-2)
    

def main():
    inputs = [
        0,
        1,
        2, #3
        3, #4
        4,
        5,
        6,
    ]

    outputs = [
        0, 
        1, 
        1, 
        2, #3
        3, 
        5, 
        8,
    ]

    for i in range(0, len(inputs)):
        assert(fib(inputs[i]) == outputs[i])

main()