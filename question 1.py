# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a += 3
# TODO: Multiply b by 2 using *=
b *= 2
# TODO: Modulo c by 4 using %=
c %= 4
#Output will be: a = 8, b = 20, c = 3
# TODO: Calculate the square root of (a^2 + b^2 + c^2)
magnitude = math.sqrt(a**2+ b**2 + c**2)
print(f"The square root of (a^2 + b^2 + c^2) is: {magnitude}")
# TODO: Print the final result rounded to 2 decimal places
print(f"The final result is: {magnitude:.2f}")
