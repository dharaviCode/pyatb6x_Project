#Create a function which takes the 3 values from the user, which are length of the triangle.
# side1, side2, side2
#i/p - int side1 == side2 =side3 → isoceles
#o/p = result in string - iso, eq, scalene

#declare/define
def triangle_type(side1, side2, side3):

   if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
   elif side1<=0 or side2<=0 or side3<=0:
       print("Not a triangle")
   else:
        print("Fails triangle inequality")

#calling function
side1 = int(input("enter the side1: "))
side2 = int(input("enter the side2: "))
side3 = int(input("enter the side3: "))

triangle_type(side1, side2, side3)
