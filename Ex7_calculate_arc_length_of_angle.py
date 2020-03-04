def achlenght():
    from math import pi

    diameter = float(input("enter the diameter of circle:"))
    angle = float(input("enter amount of angle: "))

    if angle>360:
        print("this is impossible to calculate")
    else:
        arc_lenght = (pi*diameter)*(angle/360)
        print("Arc of lenght:",arc_lenght)

achlenght()

