#create a program which shows Beep health
print("Please enter the number of lives")
lives = int(input())

print("Please enter the energy level")
energy = int(input())

print("Please enter the shield level")
shield = int(input())

print("Healt has been set.")

print(f"Lives: {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")