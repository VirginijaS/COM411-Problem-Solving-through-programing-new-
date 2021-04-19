#Code that can be used to calculate the total cost od room akeover in a house

def room_area(width, lenght):
  return width*lenght

def room_name():
  print("What is the of the room?")
  return input()

def price(name,area):
  if name == "bathroom":
    return 20*area
  elif name == "kitchen":
    return 10*area
  elif name == "bedroom":
    return 5*area 
  else:
    return 7*area

def run():
  name = room_name()
  print("What is the width of the room?")
  w = float(input())
  print("What is the lenght of the room?")
  l = float(input())
  print(f"You should pay £{price(name,room_area(w,l)):.2f}")

