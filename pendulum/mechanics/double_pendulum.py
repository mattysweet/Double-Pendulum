# -*- coding: utf-8 -*-
"""
@author: matty
"""

import numpy as np
from matplotlib import pyplot as plt
import time
from numpy import pi,cos,sin
import matplotlib.animation as animation
from pendulum.mechanics.machinery import F,G,Jminus1


def pend(l1,l2,m1,m2,theta1_init,theta2_init,thetadot1_init,thetadot2_init,g,h):

    tick=time.perf_counter() # Used for timing the calculation.

    theta1_init=(theta1_init/360)*2*pi # Convert degree input to radians
    theta2_init=(theta2_init/360)*2*pi
    
    starter=np.array([[theta1_init],[theta2_init]])
    
    p_0=np.array([[(m1+m2)*(l1**2)*thetadot1_init+m2*l1*l2*thetadot2_init*cos(theta1_init - theta2_init)],
                  [0.5*m2*(l2**2)+m2*l1*l2*thetadot1_init*cos(theta1_init-theta2_init)]]) # The Lagrangian of the double pendulum system.
        
    angles=np.array(starter)
    lastangleset=starter
    lastlastangleset=starter
    p=p_0

    count=np.array([])
    while True:
        #find the next set of angles
        a=np.arange(15)
        bestguess=2*lastangleset-lastlastangleset # Make a decent initial estimate to speed up convergence
        for j in a:
            old=bestguess
            bestguess=bestguess-np.matmul(Jminus1(lastangleset[0,0],lastangleset[1,0],bestguess[0,0],bestguess[1,0],l1,l2,m1,m2,g,h),F(lastangleset[0,0],lastangleset[1,0],bestguess[0,0],bestguess[1,0],p[0,0],p[1,0],l1,l2,m1,m2,g,h)) # Deploy variational integrator
            error=((bestguess[0,0]-old[0,0])**2 + (bestguess[1,0]-old[1,0])**2)**(1/2)
            if error<0.001: # Save on computations
                break
       
        #update p
        p=G(lastangleset[0,0],lastangleset[1,0],bestguess[0,0],bestguess[1,0],l1,l2,m1,m2,g,h)

        #store angle set
        x_1=l1*sin(bestguess[0,0])
        y_1=-l1*cos(bestguess[0,0])
        x_2=x_1+l2*sin(bestguess[1,0])
        y_2=y_1-l2*cos(bestguess[1,0])
        
        yield np.array([x_1,y_1]),np.array([x_2,y_2])
        
        thetadot1=(bestguess[0,0]-lastangleset[0,0])/h
        thetadot2=(bestguess[1,0]-lastangleset[1,0])/h
        
        #update angles
        lastlastangleset=lastangleset
        lastangleset=bestguess


class Pendulum():

    def __init__(self,
                 l1=1,l2=1,
                 m1=1,m2=1,
                 theta1=90,theta2=135,
                 thetadot1=0,thetadot2=0,
                 g=9.81,h=0.001):

        self.initial_conditions = {}
        self.initial_conditions['l1']=l1
        self.initial_conditions['l2']=l2
        self.initial_conditions['m1']=m1
        self.initial_conditions['m2']=m2
        self.initial_conditions['theta1']=theta1
        self.initial_conditions['theta2']=theta2
        self.initial_conditions['thetadot1']=thetadot1
        self.initial_conditions['thetadot2']=thetadot2
        self.initial_conditions['g']=g
        self.initial_conditions['h']=h

        self.dense_frame_ticker = 0

    def frame_generator(self):

        import json

        countr = 0

        # Convert degree input to radians
        #theta1=(self.initial_conditions['theta1']/360)*2*pi 
        #theta2=(self.initial_conditions['theta2']/360)*2*pi
        
        starter=np.array([[self.initial_conditions['theta1']],[self.initial_conditions['theta2']]])
        
        # The Lagrangian of the double pendulum system
        p_0=np.array([[(self.initial_conditions['m1']+self.initial_conditions['m2'])*(self.initial_conditions['l1']**2)*self.initial_conditions['thetadot1']+self.initial_conditions['m2']*self.initial_conditions['l1']*self.initial_conditions['l2']*self.initial_conditions['thetadot2']*cos(self.initial_conditions['theta1'] - self.initial_conditions['theta2'])],
                    [0.5*self.initial_conditions['m2']*(self.initial_conditions['l2']**2)+self.initial_conditions['m2']*self.initial_conditions['l1']*self.initial_conditions['l2']*self.initial_conditions['thetadot1']*cos(self.initial_conditions['theta1']-self.initial_conditions['theta2'])]]) 
            
        angles=np.array(starter)
        lastangleset=starter
        lastlastangleset=starter
        p=p_0

        count=np.array([])
        while True:
        #while self.dense_frame_ticker<5000:
            #find the next set of angles
            a=np.arange(15)
            bestguess=2*lastangleset-lastlastangleset # Make a decent initial estimate to speed up convergence
            for j in a:
                old=bestguess
                bestguess=bestguess-np.matmul(Jminus1(lastangleset[0,0],lastangleset[1,0],bestguess[0,0],bestguess[1,0],self.initial_conditions['l1'],self.initial_conditions['l2'],self.initial_conditions['m1'],self.initial_conditions['m2'],self.initial_conditions['g'],self.initial_conditions['h']),F(lastangleset[0,0],lastangleset[1,0],bestguess[0,0],bestguess[1,0],p[0,0],p[1,0],self.initial_conditions['l1'],self.initial_conditions['l2'],self.initial_conditions['m1'],self.initial_conditions['m2'],self.initial_conditions['g'],self.initial_conditions['h'])) # Deploy variational integrator
                error=((bestguess[0,0]-old[0,0])**2 + (bestguess[1,0]-old[1,0])**2)**(1/2)
                if error<0.001: # Save on computations
                    break
        
            # update p
            p=G(lastangleset[0,0],lastangleset[1,0],bestguess[0,0],bestguess[1,0],self.initial_conditions['l1'],self.initial_conditions['l2'],self.initial_conditions['m1'],self.initial_conditions['m2'],self.initial_conditions['g'],self.initial_conditions['h'])

            # yield pendulum positions
            x_1=self.initial_conditions['l1']*sin(bestguess[0,0])
            y_1=-self.initial_conditions['l1']*cos(bestguess[0,0])
            x_2=x_1+self.initial_conditions['l2']*sin(bestguess[1,0])
            y_2=y_1-self.initial_conditions['l2']*cos(bestguess[1,0])
            
            # update angular velocities
            #thetadot1=(bestguess[0,0]-lastangleset[0,0])/self.initial_conditions['h']
            #thetadot2=(bestguess[1,0]-lastangleset[1,0])/self.initial_conditions['h']
            
            #update angles
            lastlastangleset=lastangleset
            lastangleset=bestguess

            #print(f'frame_generator iteration {countr}: x_2={x_2}, y_2={y_2}')
            countr+=1

            yield f'\n{{"x_1":{float(x_1)},"y_1":{float(y_1)},"x_2":{float(x_2)},"y_2":{float(y_2)}}}'
            #yield float(x_2),float(y_2)

            # add to the instance frame count
            self.dense_frame_ticker+=1


    def rated_frame_generator(self, fps = 1/25):

        import re

        generator = self.frame_generator()
        frame_density = (fps) / self.initial_conditions['h']
        tick = time.perf_counter()

        rated_countr = 0

        while True:
            frame = next(generator)
            if self.dense_frame_ticker % frame_density == 0:
                if fps - (time.perf_counter() - tick) > 0:
                    time.sleep(abs(fps - (time.perf_counter() - tick)))
                tick = time.perf_counter()
                print(f'rated_frame_generator iteration {rated_countr}: x_2={frame[0]}, y_2={frame[1]}')
                rated_countr+=1
                yield frame


if __name__=='__main__':
    pend = Pendulum()

    pend = pend.rated_frame_generator()



    start = time.perf_counter()

    for i in range(250):
        frame = next(pend)
        print(i, time.perf_counter()-start)

                


        
                

    










        
"""        
tock=time.perf_counter()

crunching_time=tock-tick

print("Time taken to crunch angles: %1.4fs" %crunching_time)  # End of calculation section

tick=time.perf_counter()
x1s_e=np.array([])
for i in range(int(x1s.size/40)):
    x1s_e=np.append(x1s_e,x1s[i*40])
y1s_e=np.array([])
for i in range(int(y1s.size/40)):
    y1s_e=np.append(y1s_e,y1s[i*40])    
x2s_e=np.array([])
for i in range(int(x2s.size/40)):
    x2s_e=np.append(x2s_e,x2s[i*40])
y2s_e=np.array([])
for i in range(int(y2s.size/40)):
    y2s_e=np.append(y2s_e,y2s[i*40])

fig, ax = plt.subplots()
ax = plt.axis([-3,3,-3,3])
xs=[x2s_e[0]]
ys=[y2s_e[0]]
plt.gca().set_aspect('equal', adjustable='box')
redDot, = plt.plot([0,x1s_e[0],x2s_e[0]], [0,y1s_e[0],y2s_e[0]], 'ro-',)
greyLine, = plt.plot(xs, ys,'0.8',linewidth=1)

def animate(i):
    redDot.set_data([0,x1s_e[i],x2s_e[i]], [0,y1s_e[i],y2s_e[i]])
    x=x2s_e[i]
    y=y2s_e[i]
    xs.append(x)
    ys.append(y)
    greyLine.set_data(xs,ys)
    return redDot, greyLine,

# create animation using the above animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=x2s_e.size,
                                    interval=40, blit=False, repeat=True)
    
# Save .gif into working directory with the following name
myAnimation.save('CLICKME.gif',writer='Pillow') 

tock=time.perf_counter()
animation_time=tock-tick

print("Time taken to animate: %1.4fs"%animation_time)
print("Open CLICKME.gif in the working directory to view results")
"""    





    



