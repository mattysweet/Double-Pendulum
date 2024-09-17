# -*- coding: utf-8 -*-
"""
@author: matty
"""

import numpy as np
from numpy import sin, cos


#The following matrices were calculated using Sympy to differentiate the Lagrangian of the double pendulum


def G(theta_1_k,theta_2_k,theta_1_kplus,theta_2_kplus,l1,l2,m1,m2,g,h):
    x0 = -theta_2_k
    x1 = l1/h**2
    x2 = l2*m2*x1*(theta_2_kplus + x0)
    x3 = theta_1_kplus - theta_2_kplus
    g1=0.5*h*(-g*l1*(m1 + m2)*sin(theta_1_kplus) + 2*x1*(0.5*m1 + 0.5*m2)*(-2*theta_1_k + 2*theta_1_kplus) - x2*(-theta_1_k + theta_1_kplus)*sin(x3) + x2*cos(x3) + x2*cos(theta_1_k + x0))
    x0 = l2*m2
    x1 = h**(-2)
    x2 = -theta_2_k
    x3 = l1*x0*x1*(-theta_1_k + theta_1_kplus)
    x4 = theta_1_kplus - theta_2_kplus
    g2=0.5*h*(-g*x0*sin(theta_2_kplus) + 1.0*l2**2*m2*x1*(-2*theta_2_k + 2*theta_2_kplus) + x3*(theta_2_kplus + x2)*sin(x4) + x3*cos(x4) + x3*cos(theta_1_k + x2))
    output=np.matrix([[g1],[g2]])
    return(output)
    



def F(theta_1_k,theta_2_k,theta_1_kplus,theta_2_kplus,p_k_1,p_k_2,l1,l2,m1,m2,g,h):
    x0 = -theta_2_k
    x1 = theta_1_k + x0
    x2 = l1/h**2
    x3 = l2*m2*x2*(theta_2_kplus + x0)
    f1=0.5*h*(-g*l1*(m1 + m2)*sin(theta_1_k) + 2*x2*(0.5*m1 + 0.5*m2)*(2*theta_1_k - 2*theta_1_kplus) - x3*(-theta_1_k + theta_1_kplus)*sin(x1) - x3*cos(x1) - x3*cos(theta_1_kplus - theta_2_kplus)) + p_k_1

    x0 = l2*m2
    x1 = h**(-2)
    x2 = -theta_2_k
    x3 = theta_1_k + x2
    x4 = l1*x0*x1*(-theta_1_k + theta_1_kplus)
    f2 = 0.5*h*(-g*x0*sin(theta_2_k) + 1.0*l2**2*m2*x1*(2*theta_2_k - 2*theta_2_kplus) + x4*(theta_2_kplus + x2)*sin(x3) - x4*cos(x3) - x4*cos(theta_1_kplus - theta_2_kplus)) + p_k_2
    output=np.matrix([[f1],[f2]])
    return(output)

def Jminus1(theta_1_k,theta_2_k,theta_1_kplus,theta_2_kplus,l1,l2,m1,m2,g,h):

    x0 = 0.5*l2
    x1 = 0.25*theta_1_k
    x2 = theta_1_k - theta_2_k
    x3 = sin(x2)
    x4 = h*l1
    x5 = x3*x4
    x6 = theta_1_kplus - theta_2_kplus
    x7 = sin(x6)
    x8 = x1*x7
    x9 = 0.25*theta_1_kplus
    x10 = x7*x9
    x11 = l1*x0
    x12 = l1**2
    x13 = m1*x12
    x14 = x13*x3
    x15 = m2*x12
    x16 = x15*x3
    x17 = theta_2_k*x3
    x18 = 0.25*x17
    x19 = l1*l2**2*m2
    x20 = 0.25*x19
    x21 = theta_2_k*x7
    x22 = theta_2_kplus*x3
    x23 = theta_2_kplus*x7
    x24 = cos(x2)
    x25 = l2*x15
    x26 = 0.125*x25
    x27 = cos(x6)
    x28 = x24*x26
    x29 = theta_1_k*x3
    x30 = x26*x27
    x31 = theta_1_k*x7
    x32 = theta_1_kplus*x3
    x33 = theta_1_kplus*x7
    x34 = x25*x8
    x35 = x10*x25
    x36 = x26*x3*x7
    topleft=(h*x0 + x1*x5 + x10*x4 - x4*x8 - x5*x9)/(-m1*x11 - m2*x11 - theta_1_k**2*x36 - theta_1_kplus**2*x36 - theta_2_k**2*x36 - theta_2_kplus**2*x36 - x1*x14 - x1*x16 - x10*x13 - x10*x15 + x13*x8 + x14*x9 + x15*x8 + x16*x9 + x17*x28 + x17*x30 - x17*x34 + x17*x35 + x18*x19 + x18*x23*x25 - x20*x21 - x20*x22 + x20*x23 - x21*x28 - x21*x30 - x22*x28 - x22*x30 + x22*x34 - x22*x35 + x23*x28 + x23*x30 + x24**2*x26 + 0.25*x24*x25*x27 + x26*x27**2 - x28*x29 + x28*x31 + x28*x32 - x28*x33 - x29*x30 + x30*x31 + x30*x32 - x30*x33 + x32*x34)
    x0 = theta_1_k - theta_2_k
    x1 = cos(x0)
    x2 = 0.25*h
    x3 = theta_1_kplus - theta_2_kplus
    x4 = cos(x3)
    x5 = sin(x0)
    x6 = x2*x5
    x7 = sin(x3)
    x8 = x2*x7
    x9 = 0.5*l2
    x10 = l1*m1
    x11 = 0.25*x5
    x12 = 0.25*x7
    x13 = theta_1_k*x12
    x14 = theta_1_kplus*x10
    x15 = l1*m2
    x16 = x11*x15
    x17 = theta_1_kplus*x12
    x18 = l2*x15
    x19 = 0.125*x18
    x20 = l2**2*m2
    x21 = theta_2_k*x20
    x22 = theta_2_kplus*x20
    x23 = x1*x19
    x24 = theta_1_k*x5
    x25 = x19*x4
    x26 = theta_1_k*x7
    x27 = theta_1_kplus*x5
    x28 = theta_1_kplus*x7
    x29 = theta_2_k*x5
    x30 = theta_2_k*x7
    x31 = theta_2_kplus*x5
    x32 = theta_2_kplus*x7
    x33 = x13*x18
    x34 = x18*x29
    x35 = x19*x5*x7
    topright=(theta_1_k*x6 - theta_1_kplus*x6 + theta_2_k*x8 - theta_2_kplus*x8 - x1*x2 - x2*x4)/(-m1*x9 - m2*x9 - theta_1_k**2*x35 - theta_1_k*x10*x11 - theta_1_k*x16 - theta_1_kplus**2*x35 + theta_1_kplus*x16 - theta_2_k**2*x35 - theta_2_kplus**2*x35 + theta_2_kplus*x12*x34 + x1**2*x19 + 0.25*x1*x18*x4 + x10*x13 + x11*x14 + x11*x21 - x11*x22 - x12*x14 - x12*x21 + x12*x22 + x13*x15 - x15*x17 - x17*x18*x31 + x17*x34 + x19*x4**2 - x23*x24 + x23*x26 + x23*x27 - x23*x28 + x23*x29 - x23*x30 - x23*x31 + x23*x32 - x24*x25 + x25*x26 + x25*x27 - x25*x28 + x25*x29 - x25*x30 - x25*x31 + x25*x32 + x27*x33 - x29*x33 + x31*x33)
    x0 = theta_1_k - theta_2_k
    x1 = cos(x0)
    x2 = 0.5*h
    x3 = theta_1_kplus - theta_2_kplus
    x4 = cos(x3)
    x5 = sin(x3)
    x6 = x2*x5
    x7 = sin(x0)
    x8 = x2*x7
    x9 = 1.0*l2
    x10 = l1*m1
    x11 = 0.5*x7
    x12 = 0.5*x5
    x13 = theta_1_k*x12
    x14 = theta_1_kplus*x10
    x15 = l1*m2
    x16 = x11*x15
    x17 = theta_1_kplus*x12
    x18 = l2*x15
    x19 = 0.25*x18
    x20 = l2**2*m2
    x21 = theta_2_k*x20
    x22 = theta_2_kplus*x20
    x23 = x1*x19
    x24 = theta_1_k*x7
    x25 = x19*x4
    x26 = theta_1_k*x5
    x27 = theta_1_kplus*x7
    x28 = theta_1_kplus*x5
    x29 = theta_2_k*x7
    x30 = theta_2_k*x5
    x31 = theta_2_kplus*x7
    x32 = theta_2_kplus*x5
    x33 = x13*x18
    x34 = x18*x29
    x35 = x19*x5*x7
    bottomleft=(-theta_1_k*x6 + theta_1_kplus*x6 - theta_2_k*x8 + theta_2_kplus*x8 - x1*x2 - x2*x4)/(-m1*x9 - m2*x9 - theta_1_k**2*x35 - theta_1_k*x10*x11 - theta_1_k*x16 - theta_1_kplus**2*x35 + theta_1_kplus*x16 - theta_2_k**2*x35 - theta_2_kplus**2*x35 + theta_2_kplus*x12*x34 + x1**2*x19 + 0.5*x1*x18*x4 + x10*x13 + x11*x14 + x11*x21 - x11*x22 - x12*x14 - x12*x21 + x12*x22 + x13*x15 - x15*x17 - x17*x18*x31 + x17*x34 + x19*x4**2 - x23*x24 + x23*x26 + x23*x27 - x23*x28 + x23*x29 - x23*x30 - x23*x31 + x23*x32 - x24*x25 + x25*x26 + x25*x27 - x25*x28 + x25*x29 - x25*x30 - x25*x31 + x25*x32 + x27*x33 - x29*x33 + x31*x33)
    x0 = 1.0*h
    x1 = theta_1_k - theta_2_k
    x2 = sin(x1)
    x3 = 0.5*x2
    x4 = theta_2_k*x3
    x5 = h*l2*m2
    x6 = theta_1_kplus - theta_2_kplus
    x7 = sin(x6)
    x8 = 0.5*x7
    x9 = theta_2_k*x8
    x10 = theta_2_kplus*x5
    x11 = l2**2
    x12 = 1.0*x11
    x13 = m1*m2
    x14 = m2**2
    x15 = l1*l2*x13
    x16 = theta_1_k*x15
    x17 = theta_1_kplus*x15
    x18 = l1*x14
    x19 = l2*x18
    x20 = theta_1_k*x19
    x21 = theta_1_kplus*x19
    x22 = l2**3*x14
    x23 = theta_2_kplus*x22
    x24 = cos(x1)
    x25 = x11*x18
    x26 = 0.25*x25
    x27 = cos(x6)
    x28 = x24*x26
    x29 = theta_1_k*x2
    x30 = x26*x27
    x31 = theta_1_k*x7
    x32 = theta_1_kplus*x2
    x33 = theta_1_kplus*x7
    x34 = theta_2_k*x2
    x35 = theta_2_k*x7
    x36 = theta_2_kplus*x2
    x37 = theta_2_kplus*x7
    x38 = x25*x31
    x39 = x3*x38
    x40 = x25*x4
    x41 = x2*x26*x7
    bottomright=(m1*x0 + m2*x0 + x10*x3 - x10*x8 - x4*x5 + x5*x9)/(-theta_1_k**2*x41 - theta_1_kplus**2*x41 - theta_1_kplus*x25*x3*x37 + theta_1_kplus*x39 - theta_2_k**2*x41 - theta_2_kplus**2*x41 + theta_2_kplus*x39 - x12*x13 - x12*x14 - x16*x3 + x16*x8 + x17*x3 - x17*x8 - x20*x3 + x20*x8 + x21*x3 - x21*x8 + x22*x4 - x22*x9 - x23*x3 + x23*x8 + x24**2*x26 + 0.5*x24*x25*x27 + x26*x27**2 - x28*x29 + x28*x31 + x28*x32 - x28*x33 + x28*x34 - x28*x35 - x28*x36 + x28*x37 - x29*x30 + x30*x31 + x30*x32 - x30*x33 + x30*x34 - x30*x35 - x30*x36 + x30*x37 + x33*x40 + x37*x40 - x38*x4)
    
    
    jacobinverted=np.matrix([[topleft,topright],[bottomleft,bottomright]])
    return(jacobinverted)




