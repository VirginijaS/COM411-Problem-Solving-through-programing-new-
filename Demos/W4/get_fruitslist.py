def get_fruits():
  fruits = []
  print("How many fruits would you like to enter?")
  n = int(input())
  for i in range(n):
    print("Type in the next fruit")
    fruits.append(input())
  
  #print all items
  print("Your fruits are {}".format(fruits))

  #Print only few items by slicing
  print(f"Sliced list:{fruits[0:5:2]}")

#Print only few items by using negative Index
  print(f"Negative index: {fruits[-2:0:-1]}")

get_fruits()
