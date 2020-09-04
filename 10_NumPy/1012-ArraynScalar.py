import numpy as np

def toCelsius( f ):
    return (f-32)*5/9

def BMI( wh ):
    return np.array([ wh[n][0]/((wh[n][1]*0.01)**2) for n in range(wh.shape[0]) ])
    #no need for for loop!! 
    #just w/(h/100)**2

def distanceTo( p, Points ):
    x = (Points[::,:1] - p[0])** 2
    y = (Points[::,1:] - p[1]) ** 2
    return np.sqrt(x+y).reshape((Points.shape[0]))

exec(input().strip())