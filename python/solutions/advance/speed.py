from timeit import timeit

loop = """
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result
    
factorial(100)
"""


recursive = """
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
    
factorial(100)
"""

print("Factorial with loop: ", timeit(loop, number=100000))
print("Factorial with recursive: ", timeit(recursive, number=100000))
