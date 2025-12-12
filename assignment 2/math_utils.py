import math

def sqarea(side_length):
    return side_length ** 2
def rectarea(length, width):
    return length * width
def circlearea(radius):
    import math
    return math.pi * radius ** 2
def trianglearea(base, height):
    return 0.5 * base * height

print("choose the shape to calculate area:")
print("1. Square")
print("2. Rectangle")
print("3. Circle")
print("4. Triangle")
choice = input("Enter the number corresponding to your choice: ")
if choice == '1':
    side = float(input("Enter the side length of the square: "))
    area = sqarea(side)
    print(f"The area of the square is: {area}")
elif choice == '2':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectarea(length, width)
    print(f"The area of the rectangle is: {area}")
elif choice == '3':
    radius = float(input("Enter the radius of the circle: "))
    area = circlearea(radius)
    print(f"The area of the circle is: {area}")
elif choice == '4':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = trianglearea(base, height)
    print(f"The area of the triangle is: {area}")
else:
    print("Invalid choice. Please select a valid option.")