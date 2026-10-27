#Question 2: Complex Conditional Evaluation
#------------------------------------------------------------------------
# Task:
# Ask the user to input three integers (x, y, z).

# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50

# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))
z = int(input("Enter an integer for z: "))
# TODO: Create conditions:
#   is_even = True if x is even
#   is_positive = True if y > 0
#   is_in_range = True if z between 10 and 50
is_even = (x % 2 == 0)
is_positive = (y > 0)
is_in_range = (10 <= z <= 50)
# TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition = is_even and is_positive and is_in_range


# TODO: Print final_condition
print(f"final_condition = {final_condition}")