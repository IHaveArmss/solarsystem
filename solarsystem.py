import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Body:#poate trebuie densitatea?
    def __init__(self,mass,position,velocity,color,size):
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.color = color
        self.size = size

    def update_position(self,dt):
        self.position = self.position + self.velocity * dt


sun = Body(1.989e30,[0,0],[0,0],'yellow',15)
mars = Body(6.417e23,[227.9e9,0],[0,24.077e3],'red',5)
#creaza ploturile
fig, ax = plt.subplots()
#limitle de x,y
ax.set_xlim(-3e11,3e11)
ax.set_ylim(-3e11,3e11)

dt = 60*60 *24# 1 zi in secunde
sun_plot = ax.scatter(sun.position[0], sun.position[1], color = "yellow", s=sun.size)
mars_plot = ax.scatter(mars.position[0], mars.position[1], color = "red", s=mars.size)

bodies = [sun,mars]

def update(frame):
    for body in bodies:
        body.update_position(dt)
    
    sun_plot.set_offsets(sun.position)
    mars_plot.set_offsets(mars.position)
    return sun_plot, mars_plot

ani = FuncAnimation(fig, update, frames=365, interval=50, blit=True)

plt.show()
