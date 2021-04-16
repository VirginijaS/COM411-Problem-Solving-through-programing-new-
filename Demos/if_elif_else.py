#check weather first number is bigger than the secondnumber.
#Assume first_number and second_number are existing variables.
print("Choose an option to identify who you are?")
entity = (input())
if entity == "human":
  print("You are a human!\n")
elif entity == "robot":
  print("You are robot\n")
elif entity == "animal":
  print("You are an animal!\n")
else:
  print("I do not know what you are!\n")

print("Analysis complete")
