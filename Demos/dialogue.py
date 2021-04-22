f1 = open("john.txt")
f2 = open("harry.txt")

for i in range (3):
  print(f"\033[92mJohn: {f1.readline()}\n", end="")
  print(f"\033[93mHarry: {f2.readline()}", end="")

f1.close()