import numpy as np
import random
import matplotlib.pyplot as plot



def sinewave(x_left, x_right, x_dim, seed_number):
    '''This function takes in 4 arguments:
    1.x_left the left endpoint for the x range
    2.x_right the right endpoint for the x range
    3.x_dim the number of points between x_left and x_right.
    These points should be linearly spaced.
    4.A seed value for generating the sin waves.
    Giving the same seed should produce the same sin.

    This function returns a list with 4 elements:
    [x_axis value, y_axis value,the random amplitute, the random phase]
    '''
    random.seed(seed_number)
    # Get x values of the sine wave
    time = np.linspace(x_left, x_right, num=x_dim);
    #random phase between 0-100
    phase=random.randint(0,100)
    #random amplitute between 0-100
    random.seed(seed_number+1)
    amplitute=random.randint(0,100)
    # y values
    y = amplitute*np.sin(time-phase)
    return time, y, amplitute, phase


#plot with seed 2, X E [-2pi,2pi],x_dim=50;
x_axis,y_axis,amplitute,phase=sinewave(-6.28, 6.28, 40, 3)
plot.plot(x_axis,y_axis)
plot.ylabel("sine wave")
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()
