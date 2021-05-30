import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as r

fig, ax = plt.subplots()

def animate(frame):
  ax.cla()
  ax.set_xlim(0,10)
  ax.set_ylim(0,10)
  colours = ["r","b", "g"]
  point = "o" + colours[r.randint(0,2)]
  ax.plot(frame, frame, point)

def run():
  some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 100)
  plt.show()


run()

