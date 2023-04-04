"""Example script 01 - Demonstrate usage of package features."""

# First party modules
from lintilla import lintilla

num, result = lintilla.get_config()
exp_result = [True for i in range(num)]
print(f"Result from function 'get_config': {result}")


result = lintilla.fizzbuzz(16)
print(f"Result from function 'fizzbuzz(16)': {result}")


result = lintilla.fibonacci(10)
print(f"Result from function 'fibonacci(10)': {result}")
