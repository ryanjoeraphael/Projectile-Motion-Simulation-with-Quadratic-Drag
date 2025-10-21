'''First we add all the imports'''
import numpy as np
import math
import matplotlib.pyplot as plt

print('''Considering the fact that for a sphere the 'Drag Coefficient' is approximately equal to 0.4
and that the density of air is equal to the standard density at normal conditions which is equal to 1.225kg/m^3
''')

'''Now we add all the necessary values and calculate whats needed'''
A=float(input("Enter the area of cross section of the sphere   : "))
M=float(input("Enter the mass of the sphere                    : "))
vo=float(input("Enter the initial velocity of the projectile    : "))
ang=float(input("Enter the angle of projection of the projectile : "))
rad=(ang*math.pi)/180

k=(0.5*(1.225*0.4*A))/M
Vx=vo*math.cos(rad)
Vy=vo*math.sin(rad)

'''Were considering initial position as (0,0) at T=0 and were finding values of Vx, Yx and then
adding them to a nested list. Were taking the small change in time interval dt as 0.001 to 
maintain accuracy'''
x=0
y=0
T=0
L=[[Vx,Vy,x,y,T]]
V=vo
dt=0.001
T=0
while y>=0:
    '''This is to find acceleration, distance and velocity at that particular point'''
    ax=-k*V*Vx
    ay=-9.8-k*V*Vy
    x=x+(Vx*dt)
    y=y+(Vy*dt)
    Vx=Vx+(ax*dt)
    Vy=Vy+(ay*dt)
    V=math.sqrt((Vx**2) + (Vy**2))

    '''Now we get the total time elapsed till now by adding all the dts to a time T and then 
    adding these found values to a list which can be appended into the nested list L'''
    T=T+dt
    templist=[Vx,Vy,x,y,T]
    L.append(templist)
L.pop()
Values=np.array(L)
print(Values)
print(Values.shape)

'''Now we make a list of all the X and Y values so we can plot it all in a graph'''
Xvalues=Values[:,2]
Yvalues=Values[:,3]
plt.plot(Xvalues,Yvalues)
plt.xlabel("X coordinate of projectile")
plt.ylabel("Y coordinate of projectile")
plt.title("Graph of projectile")
plt.show()


