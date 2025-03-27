import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 6.67430e-11 #constanta gravitationala 

class Body:#poate trebuie densitatea?
    def __init__(self,mass,position,velocity,color,size):
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.color = color
        self.size = size

    def update_position(self,dt):
        self.position = self.position + self.velocity * dt
    
    def apply_gravitational_force(self,other):
        vector = other.position - self.position
        distance = np.linalg.norm(vector)

        if(distance == 0):# failsafe
            return np.array([0,0])
        force_magnitude = G * self.mass * other.mass / distance**2
        force_direction = vector/distance

        force = force_magnitude * force_direction

        return force
    
    def update_velocity(self,force,dt):
        acceleration = force/self.mass
        self.velocity = self.velocity + acceleration * dt 



sun = Body(1.989e30,[0,0],[0,0],'yellow',15)
mars = Body(6.417e23,[227.9e9,0],[0,24.077e3],'red',5)
earth = Body(5.972e24, [1.496e11, 0], [0, 29.78e3], 'green', 5)

#creaza ploturile
fig, ax = plt.subplots()
#limitle de x,y
ax.set_xlim(-3e11,3e11)
ax.set_ylim(-3e11,3e11)

dt = 60*60 *24# 1 zi in secunde
sun_plot = ax.scatter(sun.position[0], sun.position[1], color = "yellow", s=sun.size)
mars_plot = ax.scatter(mars.position[0], mars.position[1], color = "red", s=mars.size)
earth_plot = ax.scatter(earth.position[0], earth.position[1], color=earth.color, s=earth.size)

bodies = [sun,mars,earth]

def update(frame):
    for i, body1 in enumerate(bodies):
        total_force = np.array([0.0, 0.0])
        for j, body2 in enumerate(bodies):
            if i != j:  
                force = body1.apply_gravitational_force(body2)
                total_force += force 
        
        body1.update_velocity(total_force, dt)
        body1.update_position(dt)
    
    sun_plot.set_offsets(sun.position)
    mars_plot.set_offsets(mars.position)
    earth_plot.set_offsets(earth.position)

    return sun_plot, mars_plot, earth_plot

ani = FuncAnimation(fig, update, frames=365, interval=5, blit=True)

plt.show()
