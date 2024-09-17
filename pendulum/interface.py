# -*- coding: utf-8 -*-
"""
@author: matty
"""

"""               0
                 /
                /
               /
              /
             /
            /
  0--------0







This file can be run to create an animation of a double pendulum: a pendulum 
with an 'elbow' joint dividing it in two. The motion of a double pendulum is
an example of chaotic dynamics - small changes in the set up of the system lead
to very different resulting motion.

Run this file the create a CLICKME.gif of the pendulum's motion - these will be stored
in the same folder as this file. If using Spyder, access via the files tab to the right.

Alter the initial set up of the system using the parameters below.
"""

from double_pendulum import pend


l1=1                 #  Length of the upper pendulum arm.
l2=1                 #  Length of the lower pendulum arm.
m1=1                 #  Mass of the upper pendulum weight.
m2=1                 #  Mass of the lower pendulum weight.
theta1_init=90       #  Angle between upper arm and vertical. 180 degrees is pulled vertically up, 0 degrees is not pulled up at all. Increase towards 180 to raise the energy of the system
theta2_init=90      #  Angle between lower arm and vertical.
thetadot1_init=0     #  Acceleration of upper pendulum arm. A positive number is a push to the right. A negative number is a push to the left.
thetadot2_init=0     #  Acceleration of lower pendulum arm.
g=9.81           #  Strength of gravity. Earth's gravity equals 9.80665ms^-2. Moon's gravity equals 1.654 ms^-2
h=0.001              #  Timestep. The larger the timestep, the cruder the animation.
duration=5          #  Duration of created .gif in seconds.


pedulum = pend(l1,l2,m1,m2,theta1_init,theta2_init,thetadot1_init,thetadot2_init,g,h)

for i in range(250):
  print(next(pedulum))