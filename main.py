# Ask user to enter their Name amd calculate BMI
print("What is your name human?")
name = input()
print("How old are you?")
age = int(input())
print("What is your height?")
height = float(input())
print("What is your weigh?")
weight = float(input())

#Calculate bmi
bmi = weight / (height ** 2)

#Display result
print(f"{name} your bmi is {bmi}")