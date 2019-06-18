from matplotlib import pyplot as plt
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


def realArrow(x1,y1,x2,y2, proportional = True,#Estoy hasta la polla de lo rota que esta la mate
              head_width = 0.19, head_length = 0.7, fc = 'k', ec = 'k', color = 'k'):

    P = np.array([[x1,y1],[x2,y2]])
    angle = vector.angle(vector.fromPoints(P[0],P[1]))
    d = [np.cos(angle)*head_length, np.sin(angle)*head_length]
    realFpoint = P[1]-d
    fVector = vector.fromPoints(P[0],realFpoint)
    ax.arrow(P[0][0], P[0][1],
            fVector[0], fVector[1],
            head_width = head_width, head_length = head_length, color = color)

def dobleArrow(x1,y1,x2,y2, proportional = True,#proximamente MENUDO PUTO CANCER
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
