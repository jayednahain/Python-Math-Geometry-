def sector_area():
    
    from math import pi

    radious = float(input("enter the radious: "))
    angle = float(input("enter the angle: "))

    if (angle>360):
        print("the anlge is out of range ")

    else:
        area = (pi*radious**2)*(angle/360)
        print("total sector area: ",area)

sector_area()
