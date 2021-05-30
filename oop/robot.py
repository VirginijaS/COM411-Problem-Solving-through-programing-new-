from inhabitant import Inhabitant


class Robot:

  laws = "Protect, Obey and Survive"
  
  @staticmethod
  def the_laws():
    print(Robot.laws)



  def __init__(self, name="Robot", age=0):
    super().__init__(name, age)

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old and my energy is {self.energy}."

  def __repr__(self):
    return f"Robot(name = {self.name}, age = {self.age}, energy = {self.energy})"

  def display(self):
    print(f"I am {self.name}")
  
  def grow(self):
    self.age += 1

  def eat(self, ammount):
    self.energy += ammount
    if self.energy > Robot.MAX_ENERGY:
      self.energy = Robot.MAX_ENERGY

  def move(self, distance):
    self.energy -= distance
    if self.energy < 0:
      self.energy = 0

if (__name__ == "__main__"):
  robot = Robot()
  Robot.the_laws()
  print(repr(robot))
  robot.move(10)
  print(repr(robot))
  robot.eat(5)
  print(repr(robot))
  robot.eat(20)
  print(repr(robot))