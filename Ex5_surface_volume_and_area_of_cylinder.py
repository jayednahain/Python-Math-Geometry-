from math import pi 

height=float(input("enter height amount: "))
readious = float(input("enter radious amount: "))

surface_area = 2*pi*readious*height+2*pi*readious**2
total_volum = pi*readious**2*height


print("surface area of sylender: ",surface_area)
print("Total volum of sylender: ",total_volum)