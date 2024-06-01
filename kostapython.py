import math
def calculate_triangle_perimeter():
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
    perimeter = side1 + side2 + side3
    return perimeter

def calculate_square_perimeter():
    side = float(input("Enter the length of one side of the square: "))
    perimeter = 4 * side
    return perimeter

shape = input("Enter 'triangle' or 'square' to calculate its perimeter: ")

if shape == "triangle":
   perimeter = calculate_triangle_perimeter()
   print("The perimeter of the triangle is:", perimeter)
elif shape == "square":
   perimeter = calculate_square_perimeter()
print("The perimeter of the square is:", perimet
    else:
print("Invalid shape entered.")

