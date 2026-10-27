# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
base_score = int(input("Enter your base score: "))
# TODO: Apply adjustments
final_score = base_score + 5 - 10
# TODO: Clamp score between 0 and 100
final_score = max(0, min(final_score, 100))
# TODO: Use if-elif-else to determine grade and print it
if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "B"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Final Score: {final_score}")
print(f"Grade: {grade}")