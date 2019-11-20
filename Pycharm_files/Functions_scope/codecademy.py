# import math
#
# def main():
#   radius1=int(input('Please enter the circle\'s radius: '))
#   print(f'The circle is {circleArea(radius1):<.3f} sq units')
#
# def circleArea(radius):
#   area=radius**2*math.pi
#   return area
#
# main()

def main():

  input1()


def input1():
  length = input("Enter length: ")
  while length.isnumeric() is False or int(length) < 1:
    length = input('Perhaps a number this time? ')
  length = int(length)
  width = input("Enter width: ")
  while width.isnumeric() is False or int(width) < 1:
    width = input('Perhaps a number this time? ')
  width = int(width)
  height = input("Enter height: ")
  while height.isnumeric() is False or int(height) < 1:
    height = input('Perhaps a number this time? ')
  height = int(height)
  processing1(length, width, height)

def processing1(length, width, height):
  area = length * width * height
  print(f"The area of your entry is: {area}")

main()