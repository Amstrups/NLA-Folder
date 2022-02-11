#%%
import numpy as np
import matplotlib.pyplot as plt

#Opgavesæt 2:
#%%
#2.1.dist
a = np.array([0.0, 1.0])
b = np.array([1.0,-1.0])
c = np.array([-0.5, -0.8660254037844386])

aDist = np.sqrt(a[0]**2+a[1]**2)
bDist = np.sqrt(b[0]**2+b[1]**2)
cDist = np.sqrt(c[0]**2+c[1]**2)

#%%
#2.1.angle

aAngleRad = np.arctan2(a[1], a[0])
bAngleRad = np.arctan2(b[1], b[0])
cAngleRad = np.arctan2(c[1], c[0])

aAngleDegrees = np.degrees(aAngleRad)
bAngleDegrees = np.degrees(bAngleRad)
cAngleDegrees = np.degrees(cAngleRad)
# %%
#2.2
x = np.linspace(1.0, 7.0, 100)
y = (2 * np.sin(x)) / (1 + x**2)
fig, ax = plt.subplots()
ax.plot(x,y)

#%%
#2.3
x = np.linspace(-150.0, 150.0, 200)
#y = x**8-8*x**7 + 28*x**6 - 56**x**5 + 70*x**4 - 56*x**3 + 28*x**2 - 8*x + 1
z = (x-1)**8
fig, ax = plt.subplots()
#ax.plot(x,y)
#ax.plot(x,y-z)
ax.plot(x,z)


# %%
