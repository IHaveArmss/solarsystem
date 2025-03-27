import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 6.67430e-11 #constanta gravitationala 
# am decis sa il fac dictionar

def create_body (name,mass,position, velocity,color,size):
    return{
        "name": name,
        "mass": mass,
        "position": np.array(position, dtype='float64'),
        "velocity": np.array(velocity, dtype='float64'),
        "color": color,
        "size": size,
    }
#pozitia mai usor de accesat sa fac calcule
def update_position(body, dt):
    body["position"] += body["velocity"] * dt

def apply_gravitational_force(body1,body2):

    vector = body2["position"] - body1["position"]
    distance = np.linalg.norm(vector)#metoda fancy si "eficienta" sa calculezi sqrt(x^2+y^2)
    if distance == 0:#failsafe daca distanta e 0
        return np.array([0.0, 0.0])
    force_magnitude = G * body1["mass"] * body2["mass"] / distance**2
    force_direction = vector / distance
    return force_magnitude * force_direction

def update_velocity(body,force,dt):
    acceleration = force/body["mass"]
    body["velocity"] += acceleration * dt

bodies = [
    create_body("Sun",1.989e30, [0, 0], [0, 0], "yellow", 15),  #Sun
    create_body("Earth",5.972e24, [1.496e11, 0], [0, 29.78e3], "blue", 5),  #Earth
    create_body("Mars",6.417e23, [227.9e9, 0], [0, 24.077e3], "red", 5),  #Mars
    create_body("Venus",4.867e24, [1.082e11, 0], [0, 35.02e3], "orange", 5),  #Venus
    create_body("Mercury",3.285e23, [57.91e9, 0], [0, 47.87e3], "gray", 4),  # fuger mercur
]
#creaza ploturile
fig, ax = plt.subplots()
#limitle de x,y
ax.set_xlim(-3e11,3e11)
ax.set_ylim(-3e11,3e11)

plots = [ax.scatter(body["position"][0], body["position"][1], color=body["color"], s=body["size"]) for body in bodies]#crazy in line coding 👌

dt = 60*60 *12# 1 zi in secunde




def update(frame):
    for i, body1 in enumerate(bodies):
        total_force = np.array([0.0, 0.0])
        for j, body2 in enumerate(bodies):
            if i != j:  
                total_force = total_force + apply_gravitational_force(body1, body2)
            update_velocity(body1, total_force, dt)
            update_position(body1, dt)
        
    for i,plot in enumerate(plots):
        plot.set_offsets(bodies[i]["position"])

    return plots

ani = FuncAnimation(fig, update, frames=365, interval=20, blit=True)

plt.show()
