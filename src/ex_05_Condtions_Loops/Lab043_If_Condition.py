# Write a program to take a user age and
# let him know if he can go the club.
# 21

# Logic building

# Step 1
# i/p - age, int
# o/p - String(result) - Can go to club or not

# Step 2 Rough Logic (Brute force)
"""
age > 21 -> Print can go
age < 21 -> Print cannot go
age = 21 -> Print can go
"""

# Step 3 Write the logic
age = int(input("Enter age: ").strip())

if age >= 21:
    print("Can go to club")
else:
    print("Can not go to club")

# Step 4.  Check for the edge cases.
# We should consider edge cases such as:
# Negative ages or extremely high values -> program will break.
# Non-numeric input - ABC - will be handled by try-catch block
# Age which is valid. > 130

# Step 5.  Optimize the code.
# Handle all the edges.