#create a program which help Beep to paint
print("Towards which direction should I paint (up, down, left or right)?")
direction = (input())
if direction == "up":
  print("\nI am painting in the upward direction!")
elif direction == "down":
  print("\nI am painting in the downward direction")
elif direction == "left":
  print("\nI am painting in the leftward direction")
elif direction == "right\n":
  print("\nI am painting in the rightward direction")
else:
  print("not sure which direction I am painting in")