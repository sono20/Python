import numpy as np


sleep = np.array([
  [6.0, 6.0, 6.5, 8.0, 10.0, 0.0, 0.0], 
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
])


coffee = np.array([
  [1, 2, 1, 2, 1, 1, 0], 
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
])

exercise = np.array([
  [0, 0, 0, 45, 0, 45, 0], 
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
])

average1 = np.average(sleep)
average2 = np.average(coffee)
average3 = np.average(exercise)

print("My sleep average is " + str(round(average1, 2)) + " hours.")
print("My coffee intake average is " + str(round(average2, 2)) + " cups.")
print("My exercise average is " + str(round(average3, 2)) + " minutes.")
