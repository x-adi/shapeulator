import time as t
import math as m

pi = 3.14

print('''Welcome to Shapeulator...
\nThis application can do the following things - 

[-] Calculate the length of hypotenuse of a right angled triangle
[-] Calculate the length of base of a right angled triangle
[-] Calculate the length of altitude of a right angled triangle
[-] Calculate the area of a triangle


[-] Calculate the perimeter of a rectangle and a square
[-] Calculate the area of a rectangle and a square

[-] Calculate the volume of a cube and cuboid

[-] Calculate the perimeter of a circle
[-] Calculate the area of a circle

''')

def main():
    t.sleep(1)
    a=input('''\n   What do you want to do? \n
    a - Calculate the length of Hypotenuse of a right angled triangle
    b - Calculate the lenght of Base of a right angled triangle
    c - Calculate the length of Altitude of a right angled triangle
    d - Calculate the area of a triangle
    e - Calculate the perimeter of a rectangle
    f - Calculate the perimeter of a square
    g - Calculate the area of a rectangle
    h - Calculate the area of a square
    i - Calculate the volume of a cuboid
    j - Calculate the volume of a cube
    k - Calculate the perimeter of a circle
    l - Calculate the area of a circle

    Enter the corresponding alphabet here ''')

    if a =="a":
        print("\nLENGTH OF HYPOTENUSE\n")
        t.sleep(0.5)
        base_length = float(input("Enter the base length "))
        alt_length = float(input("Enter the altitude length "))
        hypotenuse_square = (base_length * base_length) + (alt_length * alt_length)
        hypotenuse = print("\nHypotenuse length is ", m.sqrt(hypotenuse_square))
        
        exp = input("\nDo you want an explanation? (y/n) ")
        t.sleep(0.20)
        if exp == "y":
            if exp == "y":
                print("\nAccording to Pythagoras Theorum, hypotenuse is equal to 'root of base square plus altitude square. So - Hypotenuse =  root of ((", base_length, "*", base_length, ") + (", alt_length, " * ", alt_length, ")) Which is ", m.sqrt(hypotenuse_square))
                t.sleep(0.5)

                t.sleep(0.5)

        else:
            print("Okay...")
            t.sleep(0.20)


        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()

        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")

        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    elif a == "b":
        print("\nLENGTH OF BASE\n")
        t.sleep(0.5)
        hypotenuse_length = float(input("Enter the hypotenuse length "))
        alt_length = float(input("Enter the altitude length "))
        if hypotenuse_length > alt_length:

            base_square = (hypotenuse_length * hypotenuse_length) - (alt_length * alt_length)
            base = print("\nBase length is ", m.sqrt(base_square))

            exp = input("\nDo you want an explanation? (y/n) ")
            t.sleep(0.23)
            if exp == "y":
                print("\nAccording to Pythagoras Theorum, base is equal to 'root of hypotenuse square minus altitude square'. So - Base = root of ((", hypotenuse_length, " * ", hypotenuse_length, " ) - (", alt_length, " * ", alt_length, ")) Which is ", m.sqrt(base_square))
            else:
                print("Okay...")
                t.sleep(0.23)

            restart = input("\nDo you want to calculate anything else? (y/n) ")
            if restart  == "y":
                t.sleep(0.5)
                main()

            elif restart == "n":
                print("\nThank You for using Shapeulator...")
                input("Press Enter Key to exit...")

            else:
                print("Invalid alphabet")
                t.sleep(0.75)
                main()

        else:
            print("\nHypotenuse length is always greater than base and altitude length. ")
            t.sleep(2)
            main()

    elif a == "c":
        print("\nLENGTH OF ALTITUDE\n")
        t.sleep(0.5)
        hypotenuse_length = float(input("Enter the hypotenuse length "))
        base_length = float(input("Enter the base length "))
        if hypotenuse_length > base_length:
            alt_square = (hypotenuse_length * hypotenuse_length) - (base_length * base_length)
            alt = print("\nAltitude length is ", m.sqrt(alt_square))

            exp = input("\nDo you want an explanation? (y/n)")
            if exp == "y":
                print("\nAccording to Pythagoras Theorum, altitude is equal to 'root of hypotenuse square - base square'. So - Altitude = root of ((", hypotenuse_length, " * ", hypotenuse_length, " ) - ( ", base_length, " * ", base_length, ")) Which is ", m.sqrt(alt_square), ".")
                t.sleep(0.5)

            else:
                print("Okay...")
                t.sleep(0.25)

            restart = input("\nDo you want to calculate anything else? (y/n) ")
            if restart  == "y":
                t.sleep(0.5)
                main()

            elif restart == "n":
                print("\nThank You for using Shapeulator...")
                input("Press Enter Key to exit...")

            else:
                print("Invalid alphabet")
                t.sleep(0.75)
                main()

        else:
            print("\nHypotenuse length is always greater than base and altitude length. ")
            t.sleep(2)
            main()

    elif a == "d":
        print("\nAREA OF A TRIANGLE\n")
        t.sleep(0.5)
        base_length = float(input("Enter the base length "))
        alt_length = float(input("Enter the altitude length "))
        area = print("\nArea of the triangle is ", 1/2 * base_length * alt_length)

        exp = input("\nDo you want an explanation? (y/n) ")
        if exp == "y":
            print("\nThe formula of calculating area of a triangle is 1/2 bh that is 1/2 * b * h. So, 1/2 * ", base_length, "* ", alt_length, "is ", 1/2 * base_length * alt_length, ".")
            t.sleep(0.24)

        else:
            print("Okay...")
            t.sleep(0.5)

        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()

        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")

        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    elif a == "e":
        print("\nPERIMETER OF A RECTANGLE\n")
        t.sleep(0.5)
        length = float(input("Enter the length of the rectangle "))
        breadth = float(input("Enter the breadth of the rectangle "))
        perimeter = print("\nPerimeter of the rectangle is ", 2 * (length + breadth))

        exp = input("\nDo you need an explanation? (y/n) ")
        if exp == "y":
            print("The formula of calculating the perimeter of a rectangle is 2 * (length + breadth) that is 2 * (", length, " + ", breadth, "). So ", 2 * ( length + breadth))
            t.sleep(0.23)

        else:
            print("Okay..")
            t.sleep(0.5)

        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()

        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")

        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    elif a == "f":
        print("\nPERIMETER OF A SQUARE\n")
        t.sleep(0.5)
        side = float(input("Enter the length of a side "))
        perimeter = print("\nPerimeter is ", 4 * side)

        exp = input("\nDo you need an explanation? (y/n) ")
        if exp == "y":
            print("\nThe formula of calculating the perimeter of a square is 4 * side. So 4 * ",side, " = ", 4 * side)
            t.sleep(0.23)

        else:
            print("Okay...")
            t.sleep(0.20)

        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()
        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")
        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    elif a == "g":
        print("\nAREA OF A RECTANGLE\n")
        t.sleep(0.5)
        length = float(input("Enter the length of the rectangle "))
        breadth = float(input("Enter the breadth of the rectangle "))
        area = print("\nArea of the rectangle is ", length * breadth)

        exp = input("\nDo you need an explanation? (y/n) ")
        if exp == "y":
            print("\nThe formula to calculate the area of a triangle is length * breadth that is ", length, " * ", breadth, ". So - Area = ", length * breadth)
            t.sleep(0.5)

        else:
            print("Okay...")
            t.sleep(0.23)

        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()
        
        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")
        
        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    elif a == "h":
        print("\nAREA OF A SQUARE\n")
        t.sleep(0.5)
        side = float(input("Enter the side of the square "))
        area = print("The area of the square is ", side * side)

        exp = input("\nDo you need an explanation? (y/n) ")
        if exp == "y":
            print("\nThe formula to calculate the area of a square is side * side that is ", side, " * ", side, ". So area is ", side * side )
            t.sleep(0.5)

        else:
            print("Okay...")
            t.sleep(0.20)

        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()
        
        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")
        
        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    elif a == "i":
        print("\nVOLUME OF A CUBOID\n")
        t.sleep(0.5)
        length = float(input("Enter the length of the cuboid "))
        breadth = float(input("Enter the breadth of the cuboid "))
        height = float(input("Enter the height of the cuboid "))
        volume = print("\nVolume of the cuboid is ", length * breadth * height)

        exp = input("\nDo you need an explanation? (y/n) ")
        if exp == "y":
            print("\nThe formula to calculate the volume of a cuboid is l * b * h that is ", length, " * ", breadth, " * ", height, ". So volume is ",length * breadth * height)
            t.sleep(0.5)

        else:
            print("Okay...")
            t.sleep(0.23)

        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()
        
        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")
        
        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    elif a == "j":
        print("\nVOLUME OF A CUBE\n")
        t.sleep(0.5)
        side = float(input("Enter the side of the cube "))
        volume = print("\nVolume of the cube is ", side * side * side)

        exp = input("\nDo you need an explanation? (y/n) ")
        if exp == "y":
            print("\nThe formula to calculate the volume of cube is 'side cube' that is ", side, " * ", side, " * ", side, ". So volume is ", side * side * side)
            t.sleep(0.5)

        else:
            print("Okay...")
            t.sleep(0.23)

        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()
        
        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")
        
        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    elif a == "k":
        print("\nPERIMETER OF A CIRCLE\n")
        t.sleep(0.5)
        radius = float(input("Enter the radius of the circle "))
        perimeter = print("\nPerimeter of the circle is ", 2 * pi * radius)

        exp = input("Do you need an explanation? (y/n) ")
        if exp == "y":
            print("The formula to calculate the perimeter of a circle is 2 * 3.14 (pi) * r that is 2 * 3.14 * ", radius, ". So the perimeter is ", 2 * pi * radius)
            t.sleep(0.5)

        else:
            print("Okay...")
            t.sleep(0.23)

        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()
        
        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")
        
        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    elif a == "l":
        print("\nAREA OF A CIRCLE\n")
        t.sleep(0.5)
        radius = float(input("Enter the radius of the circle "))
        area = print("\nArea of the circle is ", pi * radius * radius)

        exp = input("Do you need an explanation? (y/n) ")
        if exp == "y":
            print("The formula to calculate the area is pi * r * r that is ", pi ," * ", radius, " * ", radius, ". So area of the circle is ", pi * radius * radius)
            t.sleep(0.5)

        else:
            print("Okay")

        restart = input("\nDo you want to calculate anything else? (y/n) ")
        if restart  == "y":
            t.sleep(0.5)
            main()
        
        elif restart == "n":
            print("\nThank You for using Shapeulator...")
            input("Press Enter Key to exit...")
        
        else:
            print("Invalid alphabet")
            t.sleep(0.75)
            main()

    else:
        print("Invalid alphabet...")
        t.sleep(0.75)
        main()
main()
