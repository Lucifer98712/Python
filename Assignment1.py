'''
A drunk person is walking along (2 dimensional plane/ 3d space). Calculate average distance (displacement) 
covered after 1000 steps.
Simulate this with at least 1000 iterations using software of your choice to calculate max displacement
and average dispacement and present 1 moment graphically.
'''
import matplotlib.pyplot as plt    
import numpy as np
import random
import math

def drunk_walk(n):
    x = np.zeros(n) 
    y = np.zeros(n) 

    directions = ["up", "down", "left", "right"] 

    for i in range(1,n): 
        step = random.choice(directions) 

        
        if step == "up":
            x[i] = x[i-1]       
            y[i] = y[i-1] + 1   

        elif step == "down":
            x[i] = x[i-1]        
            y[i] = y[i-1] - 1    

        elif step == "right":
            x[i] = x[i-1] + 1   
            y[i] = y[i-1]

        elif step == "left":
            x[i] = x[i-1] - 1   
            y[i] = y[i-1]

    return x, y                 


#1000 iteration of random walk
displacement = np.zeros(1000)   
for i in range(0,1000):
    x_data,y_data = drunk_walk(1000) 

    a = x_data[999] - x_data[0]
    b = y_data[999] - y_data[0]
    displacement[i] = math.sqrt(a*a + b*b)

avg_displacement = sum(displacement) / len(displacement)
max_displacement = max(displacement)
print("------ In 1000 iteration ------")
print("Avg Displacement = " + str(avg_displacement))
print("Max Displacement = " + str(max_displacement))

#plotting a moment of the drunk man walking
x_data,y_data = drunk_walk(1000) 
plt.title("A drunk person's walk:")
plt.plot(x_data,y_data)
plt.xlabel("x-axis:")
plt.ylabel("y-axis:")
plt.grid()

#plotting displacement for this moment
print("\n------- One moment --------")
print(f"initial position = ({x_data[0]},{y_data[0]})")
print(f"final position = ({x_data[999]},{y_data[999]})")
x_values = [x_data[0], x_data[999]]
y_values = [y_data[0], y_data[999]]
plt.plot(x_values, y_values, marker='o',color='r', linestyle='--')

plt.show()
