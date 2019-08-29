import os
import math
import shutil
print("Hello world")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = b*b-4*a*c
if d<0:
    print("Корней нет")
elif d==0:
    print("Корень: ", (-b+math.sqrt(d))/2)
else:
    print("Корень1: ", (-b+math.sqrt(d))/(2*a) )
    print("Корень2: ", (-b-math.sqrt(d))/(2*a) )


#print("Привет ", name)
#print(os.listdir())