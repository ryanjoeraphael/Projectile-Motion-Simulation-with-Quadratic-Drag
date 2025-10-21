# Projectile-Motion-Simulation-with-Quadratic-Drag
Overview

This project provides a numerical solution to the classical physics problem of a projectile launched into the air while subject to a quadratic drag force (air resistance proportional to the square of the velocity). This scenario results in a system of coupled, non-linear differential equations that cannot be solved with a simple closed-form analytical expression.

The script uses a computational approach to determine the projectile's velocity and position at any time t.

Methodology: Euler's Method

To solve the system of differential equations, the simulation employs Euler's Method. This is a first-order numerical procedure for solving ordinary differential equations (ODEs) with a given initial value.

The continuous differential equations are discretized and solved iteratively over a small time step ($\Delta t$). For each step, the acceleration is calculated based on the current velocity, and that acceleration is used to extrapolate the new velocity and position:

Variable        Governing Equation
Vx              d(Vx)/dt = Ax(Vx,Vy)
Vy              d(Vy)/dt = Ay(Vx,Vy) - g
x,y             d(x)/dt = Vx , d(y)/dt = Vy

The iteration uses the following update rules:

V(t+dt) = v(t) + a(t)dt
r(t+dt) = r(t) + v(t)dt

The use of a small, appropriate time step dt is critical to ensure the stability and accuracy of the solution.

Initial Parameters

Parameter                         Value        
mass(m)                           2kg
cross sectional area(A)           1m^2
Drag Coefficient (Cd)             0.4
Initial velocity (Vo)             20m/s
Launch Angle(theta)               45 degrees

Output

The program successfully outputs the following results:

Arrays of Vx(t), Vy(t), x(t), and y(t) values.
The Time of Flight (T), found by interpolating the discrete steps where the vertical position y(t) crosses the y=0 boundary.
A plot of the trajectory comparing the path with drag to the idealized parabolic path without drag.
