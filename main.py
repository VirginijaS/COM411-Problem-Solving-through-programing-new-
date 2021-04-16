#check weather first number is bigger than the secondnumber.
#Assume first_number and second_number are existing variables.
print("Can you write first number?")
a = int(input())
print("Can you write second number?")
b = int(input())
if a  > b:
  print("First is bigger\n")
elif a < b:
  print("First is smaller\n")
else:
  print("Both are equal\n")

print("Done")
