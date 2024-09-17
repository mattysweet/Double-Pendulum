from flask import Blueprint, render_template, request, redirect, url_for
import numpy as np

from pendulum.mechanics.double_pendulum import Pendulum

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("base.html")

@bp.route("/stream_coordinates",methods = ["POST"])
def stream_coordinates():

    print('registered')

    ic = request.get_json()

    theta1 = np.arctan2(ic['y1'],ic['x1']) - 3/2 * np.pi
    theta2 = np.arctan2(ic['y2']-ic['y1'],ic['x2']-ic['x1']) - 3/2 * np.pi


    #theta1 = np.pi / 2
    #theta2 = np.pi
    """
    pend(l1 = 1,l2 = 1,
                    m1 = 1, m2 = 1,
                    theta1_init = theta1, theta2_init = theta2,
                    thetadot1_init = 0, thetadot2_init = 0,
                    g = 9.81, h = 0.001,
                    duration = 5)
    
    return 'hi'

    """    

    #print(360*theta1/(2*np.pi), 360*theta2/(2*np.pi))
    #"""
    pend = Pendulum(l1 = ic['l1'],l2 = ic['l2'],
                    m1 = 1, m2 = 1,
                    theta1 = theta1, theta2 = theta2,
                    thetadot1 = 0, thetadot2 = 0,
                    g = 9.81, h = 0.001
                    )

    pend = pend.rated_frame_generator()

    #for i in range(75):
    #    next(pend)

    return pend

    #print('ready to send')
    #"""


import numpy as np
from matplotlib import pyplot as plt
import time
from numpy import pi,cos,sin
import matplotlib.animation as animation
from pendulum.mechanics.machinery import F,G,Jminus1


def pend(l1,l2,m1,m2,theta1_init,theta2_init,thetadot1_init,thetadot2_init,g,h,duration):

    tick=time.perf_counter() # Used for timing the calculation.

    #theta1_init=(theta1_init/360)*2*pi # Convert degree input to radians
    #theta2_init=(theta2_init/360)*2*pi
    
    starter=np.array([[theta1_init],[theta2_init]])
    
    p_0=np.array([[(m1+m2)*(l1**2)*thetadot1_init+m2*l1*l2*thetadot2_init*cos(theta1_init - theta2_init)],
                  [0.5*m2*(l2**2)+m2*l1*l2*thetadot1_init*cos(theta1_init-theta2_init)]]) # The Lagrangian of the double pendulum system.
        
    b=np.arange(1000*duration)
    angles=np.array(starter)
    lastangleset=starter
    lastlastangleset=starter
    p=p_0
    x1s=np.array([])
    y1s=np.array([])
    x2s=np.array([])
    y2s=np.array([])
    count=np.array([])
    for i in b:
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
        
        x1s=np.append(x1s,x_1)
        y1s=np.append(y1s,y_1)
        x2s=np.append(x2s,x_2)
        y2s=np.append(y2s,y_2)
        
        thetadot1=(bestguess[0,0]-lastangleset[0,0])/h
        thetadot2=(bestguess[1,0]-lastangleset[1,0])/h
        
        #update angles
        lastlastangleset=lastangleset
        lastangleset=bestguess
        
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