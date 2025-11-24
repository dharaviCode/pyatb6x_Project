# Triangle Classifier:

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.


def classify_triangle(a, b, c):

  if a > 0 and b > 0 and c > 0:
    if a+b > c and b+c > a and c+b > a:
       if a == b == c:
        return "Equilateral triangle"
       elif a == b or a == c or b == c:
        return "Isosceles triangle"
       else:
        return "Scalan triangle"
    else:
        print("Not a triangle")

  else:
       print("Not a valid length")


result = classify_triangle(2, 2, 3)
print(result)



