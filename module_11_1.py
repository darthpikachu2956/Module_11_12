import numpy as np

# Task with numpy
massive = np.array([1, 2, 3, 4, 5])
massive_2 = np.arange(5)
mass_3 = massive * massive_2

print(massive)
print(massive_2)
print(mass_3)

massive[1] = 7
mass_4 = massive ** 2
print(mass_4)

reshaped_1 = massive.reshape(5, 1)
print(reshaped_1)
print(massive_2.min(), ',', massive.sum(), '\n')
###########################################
import matplotlib.pyplot as mp

# Task with matplotlib
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

mp.plot(x, y, marker='o')
mp.title('Example')
mp.xlabel('x')
mp.ylabel('y')
mp.grid(True)
mp.show()
###########################################
from PIL import Image

# Task with pillow
img = Image.open("5.jpg")
img2 = img.resize((300, 500))
img2.save("7.png")
img3 = img2.crop((25, 25, 100, 100))
img3.save("8.png")
img4 = img2.rotate(90)
img4.save("9.png")
img.show()
