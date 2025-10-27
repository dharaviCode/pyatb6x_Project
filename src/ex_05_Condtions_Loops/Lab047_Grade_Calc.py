# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Step 1
# i/p - score, int
# o/p - String value (A, B, C, D, E, F)

# Step 2 Rough logic
# 90 < Score < 100 - A
# 80 < Score < 89 - B
# 70 < Score < 79 - C
# 60 < Score < 69 - D
# Score < 59 - F

# Step 3 Logic building

score = float(input("Score achieved: ").strip())
score = round(score, 2)  # Rounds to 2 decimal places

if score >= 0 and score <= 100:

 if score >= 90 and score <= 100:
    print("Grade received", "A")
 elif score >= 80 and score < 90:
    print("Grade received", "B")
 elif score >= 70 and score < 80:
    print("Grade received", "C")
 elif score >= 60 and score < 70:
    print("Grade received", "D")
 else:
    print("Grade received", "F")

else:
    print("Invalid Grade!")

# This code handles the "floating-point precision issue".
# >>> float(69.999999999999999)
# 70.0
# So the condition elif score >= 70 and score < 80: becomes True, hence Grade C instead of D.
# This isn’t a logic issue — it’s a floating-point rounding issue.
