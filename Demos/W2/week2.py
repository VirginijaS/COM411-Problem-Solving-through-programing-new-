#Program that displays a menu and allows the user to either see a nice message, calculate areas of rectangle or triangle or display a times for a number.

print("Please choose and option from the menu:\n\n1-Nice message\n2-Area of rectangle\n3-Area of triangle\n4-Time table")

option = int(input())

if option ==1:
  print("Today will be nice day")
elif option == 2:
  print("Enter the length of the rectangle:")
  l = int(input())
  print("Enter the width of the rectangle:")
  w = int(input())
  area = l*w
  print("The area of this rectangle was {}". format(area))
elif option == 3:
  print("Enter the base of the triangle:")
  base = float(input())
  print("Enter the height of the triangle:")
  height = float(input())
  area = 0.5*base*height
  print("The area of this triangle was {:.2f}". format(area))
elif option == 4:
  print("What number would you like to see time table for?")
  n = int(input())
  for i in range(1,11,1):
    print("{}x{} = {}". format(n,i,n*i))
else:
  print("There is no such option. Go to specsavers!")


