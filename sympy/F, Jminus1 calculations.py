# -*- coding: utf-8 -*-
"""
Created on Tue May  4 08:05:18 2021

@author: matty
"""

import sympy as sp
from sympy import symbols, sin, cos, Array, diff, nonlinsolve, pi, Matrix, cse
from matplotlib import pyplot as plt

from sympy.utilities.lambdify import lambdify

theta_1_k , theta_2_k , theta_1_kplus, theta_2_kplus = symbols('theta_1_k  theta_2_k  theta_1_kplus theta_2_kplus')
l1 , l2 , m1, m2, g, h = symbols('l1 l2 m1 m2 g h')

theta_k=Array([theta_1_k, theta_2_k])
theta_kplus=Array([theta_1_kplus,theta_2_kplus])

p_k_1,p_k_2 , p_kplus_1 , p_kplus_2= symbols('p_k_1 p_k_2 p_kplus_1 p_kplus_2')

def lagrangian(theta,thetadot):
    return 0.5*(m1+m2)*l1*thetadot[0]**2 + 0.5*m2*(l2**2)*thetadot[1]**2+m2*l1*l2*thetadot[0]*thetadot[1]*cos(theta[0]-theta[1])+(m1+m2)*g*l1*cos(theta[0])+m2*g*l2*cos(theta[1])

def ldtrap(theta_old,theta_new):
    return(0.5*h*(lagrangian(theta_old,(theta_new-theta_old)/h)+lagrangian(theta_new,(theta_new-theta_old)/h)))


f1=p_k_1+diff(ldtrap(theta_k,theta_kplus),theta_1_k)
f2=p_k_2+diff(ldtrap(theta_k,theta_kplus),theta_2_k)

g1=diff(ldtrap(theta_k,theta_kplus),theta_1_kplus)
g2=diff(ldtrap(theta_k,theta_kplus),theta_2_kplus)
gee=Matrix([g1,g2])

G=lambdify([theta_1_k,theta_2_k,theta_1_kplus,theta_2_kplus,l1,l2,m1,m2,g,h],gee,"numpy")

f=Matrix([f1,f2])

jacob=Matrix([[diff(f1,theta_1_kplus),diff(f1,theta_2_kplus)],[diff(f2,theta_1_kplus),diff(f2,theta_2_kplus)]])

jacobinverted=jacob**-1

repl, redu = cse(jacobinverted[0,0])
for variable, expr in repl:
    print(f"{variable} = {expr}")
print("topleft")
print(redu[0])


repl, redu = cse(jacobinverted[0,1])
for variable, expr in repl:
    print(f"{variable} = {expr}")
print("topright")
print(redu[0])


repl, redu = cse(jacobinverted[1,0])
for variable, expr in repl:
    print(f"{variable} = {expr}")
print("bottomleft")
print(redu[0])

repl, redu = cse(jacobinverted[1,1])
for variable, expr in repl:
    print(f"{variable} = {expr}")
print("bottomright")
print(redu[0])

Jminus1=lambdify([theta_1_k,theta_2_k,theta_1_kplus,theta_2_kplus,l1,l2,m1,m2,g,h],jacobinverted,"numpy")
F=lambdify([theta_1_k,theta_2_k,theta_1_kplus,theta_2_kplus,p_k_1,p_k_2,l1,l2,m1,m2,g,h],f,"numpy")





