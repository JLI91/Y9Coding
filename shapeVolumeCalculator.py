# Importing the Math Module
import math

# This is the non-graphical UI
print ("This program will find the volume of a chosen shape.")
choice = float(input("Please choose a shape\n1 for cube,\n2 for sphere,\n3 for cone,\n4 for cylinder\n5 for Rectangular Prism. \n"))

if choice == 1:
  length = float(input("Please type the side length of this cube. \n"))
  rounding = int(input("Please type in the number of decimals you want to round to. \n"))
  volumeOfCube = str(round(length * length * length, rounding))
  print ("The volume of this cube is " + volumeOfCube + " units cubed.")
elif (choice == 2):
  radius = float(input("Please type the radius of this sphere. \n"))
  rounding = int(input("Please type in the number of decimals you want to round to. \n"))
  volumeOfSphere = str(round(math.pi * 4/3 * radius * radius * radius, rounding))
  print ("The volume of this cube is " + volumeOfSphere + " units cubed.")
elif (choice == 3):
  radius = float(input("Please type the radius of this cone. \n"))
  height = float(input("Please type in the height of this cone \n"))
  rounding = int(input("Please type in the number of decimals you want to round to. \n"))
  volumeOfCone = str(round(math.pi * radius * radius * height/3, rounding))
  print ("The volume of this cube is " + volumeOfCone + " units cubed.")
elif (choice == 4):
  radius = float(input("Please type the radius of this cylinder. \n"))
  height = float(input("Please type in the height of this cylinder \n"))
  rounding = int(input("Please type in the number of decimals you want to round to. \n"))
  volumeOfCylinder = str(round(math.pi * radius * radius * height, rounding))
  print ("The volume of this cube is " + volumeOfCylinder + " units cubed.")
elif (choice == 5):
  length = float(input("Please type the lenght of this rectangular prism. \n"))
  width = float(input("Please type the width of this rectangular prism. \n"))
  height = float(input("Please type the heigh of this rectangular prism. \n"))
  rounding = int(input("Please type in the number of decimals you want to round to. \n"))
  volumeOfRectPrism = str(round(length * width * height, rounding))
else:
  # If the user enters a value that isn't listed
    print ("This is not a valid choice")
