from rectangle import Rectangle
from circle import Circle


cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
cirkel2 = Circle(x=1,y=1, radius=1)
rektangel = Rectangle(x=0,y=0,width=1, length=1)


print(f'{cirkel1==cirkel2 = }') # True
print(f'{cirkel2==rektangel = }') # False
print(f'{cirkel1.is_inside(0.5, 0.5) = }') # True
cirkel1.translate(5,5)
print("cirkel1.translate(5,5)")

print(f'{cirkel1.is_inside(0.5, 0.5) = }') # False

try: 
    cirkel1.translate("TRE",5)
    
except TypeError:
    print(f'you have entered the wrong datatype')