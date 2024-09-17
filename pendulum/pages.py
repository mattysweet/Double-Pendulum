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

    pend = pend.rated_frame_generator(fps=1/100)

    #for i in range(75):
    #    next(pend)

    return pend

    #print('ready to send')
    #"""