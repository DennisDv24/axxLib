from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
from axx.twodgem import *

ax = plt.axes()

def limitAxes(x1=0, x2=0, y1 = 0, y2 = 0,
              automatic = False, scaleRatio = 0):

    if(automatic==False):
        if(x1==0 and x2 == 0 and y1 == 0 and y2 == 0):
            print('E: set x and y limit')
        if(y1 == 0 and y2 == 0):
            y1 = x1; y2 = x2
        axes = plt.gca()
        axes.set_xlim([x1,x2])
        axes.set_ylim([y1,y2])

    if(scaleRatio != 0):
        if(scaleRatio == 'square'):
            plt.gca().set_aspect((x2-x1)/(y2-y1))
        else:
            plt.gca().set_aspect(scaleRatio)


def realArrow(x1,y1,x2,y2, proportional = True,
              head_width = 0.19, head_length = 0.7, fc = 'k', ec = 'k', color = 'k'):

    P = np.array([[x1,y1],[x2,y2]])
    angle = vector.angle(vector.fromPoints(P[0],P[1]))
    d = [np.cos(angle)*head_length, np.sin(angle)*head_length]
    realFpoint = P[1]-d
    fVector = vector.fromPoints(P[0],realFpoint)
    ax.arrow(P[0][0], P[0][1],
            fVector[0], fVector[1],
            head_width = head_width, head_length = head_length, color = color)

#def dahsedLine(x1,y1,x2,y2, color = 'k'):
#    ax.arrow(x1,y1,x2-x1,y2-y1,ls = 'dashed',arrowstyle = '-',head_width = 0, head_length = 0, color = color)

def dobleArrow(x1,y1,x2,y2, proportional = True,
               head_width = 0.19, head_length = 0.7, fc='k', ec='k'):

    P = [[x1,y1],[x2,y2]]
    dist = vector.fromPoints(P[1],P[0])


    angle = vector.angle(dist)*-1
    arrDist = vector.fromModule(head_length, angle)

    realPoints = [P[0], P[1]]
    realDist = dist-2*arrDist
    #arrdist se mantiene


    ax.arrow(realPoints[0][0],realPoints[0][1],
        -realDist[0],-realDist[1],
        head_width = head_width, head_length = head_length, fc=fc, ec=ec)
    ax.arrow(realPoints[1][0],realPoints[1][1],
        realDist[0],realDist[1],
        head_width = head_width, head_length = head_length, fc=fc, ec=ec)


def hideAxes():
    ax.set_xticklabels([])
    ax.set_yticklabels([])

def gridDensity():#Dont know how this works lol

    major_ticks = np.arange(-15, 15, 2)
    minor_ticks = np.arange(-15, 15, 20)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='both')

    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

def xANDy(lim,xaxpos,yaxpos, font = 22):
    x = np.zeros((2,10))
    y = np.zeros((2,10))
    x[0] = np.linspace(-lim,lim,10)
    y[0] = x[0]*0
    y[1] = np.linspace(-lim,lim,10)
    x[1] = y[0]*0
    plt.text(xaxpos[0],xaxpos[1],r'$x$')
    plt.text(yaxpos[0],yaxpos[1],r'$y$')
    plt.plot(x[0],y[0],x[1],y[1], color = 'k');


def DDlinearTransform(ran=10,matrix = [[1,0],[0,1]],
                      colorFunction = (1,1,1),
                      head_width = 0.15, head_length = 0.7,
                      vector = True,
                      factor = 0.1):
    red=1
    green=0
    blue=0
    canRed, canGreen, canBlue = True,False,False
    T = np.zeros((ran*2,ran*2,2))
    n=0
    for i in range(-ran,ran+1):
        for j in range(-ran,ran+1):
            T[i,j] = [i,j]
            T[i,j] = np.dot(matrix,T[i,j])
    for i in range(-ran-1,ran):
        for j in range(-ran-1,ran):
            #print(red)
            #print(green)
            #print(blue)
            #print('-----------')FIXFIXFIXFIXFIX

            # if(canRed):
            #     red-=factor #Why dont work?
            #     green+=factor
            #     if(red <= 0): canRed = False; canGreen = True; red = 0;green = 1
            # if(canGreen):
            #     green-=factor
            #     blue+=factor
            #     if(green <= 0): canGreen = False; canBlue = True; green = 0;blue = 1
            # if(canBlue):
            #     blue-=factor
            #     red+=factor
            #     if(blue <= 0): canBlue = False; canRed = True; blue = 0;red = 1

            #if((red>=0and green>=0and blue>=0) and (red<=1and green<=1and blue<=1)):
            #if(vector):
            realArrow(0,0,T[i,j,0],T[i,j,1],head_width=0.15, color = (red,green,blue))
            # else:
            #     plt.scatter(T[:,:,0],T[:,:,1], color = (red,green,blue))
            #     plt.text(T[i,j,0],T[i,j,1],n)
            # n+=1
