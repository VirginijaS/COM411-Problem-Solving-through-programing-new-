#While loop (and also FOR loop) can be used to have a repetition of a procedure in our chr

print("How many times to print the symbol?")
x = int(input())

#i is a counter - it keeps track of how many times we went through the loop
i = 0

while i < x: #condition for repetaing the code - as long as i lower than x
  print("\u27BD \n")
  i = i + 1 #new value of the counter is one more than it used to be

print("We left the loop")