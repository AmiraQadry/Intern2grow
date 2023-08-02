import math

def calculate_square_area(side):
    return side ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

print("Welcome to the Area Calculator!")

while True:
    print("\nPlease select an option:")
    print("1. Calculate the area of a square")
    print("2. Calculate the area of a rectangle")
    print("3. Calculate the area of a circle")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        side = float(input("Enter the length of a side: "))
        area = calculate_square_area(side)
        print("The area of the square is:", area)
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print("The area of the rectangle is:", area)
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print("The area of the circle is:", area)
    elif choice == '4':
        print("Thank you for using the Area Calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")