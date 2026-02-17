# Area Calculator!

UseAgain = "Y"
while UseAgain == "Y":
  print("==================================")
  print("Welcome to the Area Calculator! 📐")
  print("==================================")

  print("The shapes available on this calculator are:")
  print("  1. Square")
  print("  2. Rectangle")
  print("  3. Triangle")
  print("  4. Circle")

  shape = int(input("Please select the shape you'd like to calculate the area for (1-4): "))

# Shape selection and area calculations
  while shape < 1 or shape > 4:
     shape = int(input("Invalid shape selection. Please select a number between 1 and 4: "))
  if shape == 1:
      print("You have selected a: Square")
      side = float(input("Please enter the length of a side of your square: "))
      area = side * side
      print(f"The area of your square is: {area}")
  elif shape == 2:
      print("You have selected a: Rectangle")
      length = float(input("Please enter the length of your rectangle: "))
      width = float(input("Please enter the width of your rectangle: "))
      area = length * width
      print(f"The area of your rectangle is: {area}")
  elif shape == 3:
      print("You have selected a: Triangle")
      base = float(input("Please enter the length of the base of your triangle: "))
      height = float(input("Please enter the height of your triangle: "))
      area = 0.5 * base * height
      print(f"The area of your triangle is: {area}")
  else:
      print("You have selected a: Circle")
      radius = float(input("Please enter the radius of your circle: "))
      area = 3.14 * (radius * radius)
      print(f"The area of your circle is: {area}")

  UseAgain = input("Would you like to use me again? (Y/N): ")
if UseAgain == "Y":
  print("Nice! Let's go again!")
else:
  print("Thank you for using the area calculator! Goodbye! 👋")

# This could turn the value of UseAgain to "N".
# If this is the case, the loop will END as the condition for the loop to continue is now false.