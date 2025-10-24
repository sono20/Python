import numpy as np

egg_carton1 = np.array([
  [0.89, 0.90, 0.83, 0.89, 0.97, 0.98], 
  [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]
])
  
egg_carton2 = np.array([
  [0.89, 0.95, 0.84, 0.92, 0.94, 0.93], 
  [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]
])
  
egg_carton3 = np.array([
  [0.83, 0.95, 0.89, 0.54, 0.37, 0.92], 
  [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]
])

average1 = np.average(egg_carton1)
average2 = np.average(egg_carton2)
average3 = np.average(egg_carton3)

print(average1)
print(average2)
print(average3)