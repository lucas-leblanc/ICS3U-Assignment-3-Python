# Copyright (c) 2022 Lucas LeBlanc All rights reserved.
#
# Created by: Lucas LeBlanc
# Created on: Oct 2022
# This program tells you what type of triangle you have picked

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")

print("\n\nDone.")
