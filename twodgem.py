import numpy as np

class vector:
    def module(v):
        val = 0
        for i in range(0,len(v)):
            val+=v[i]**2
        return np.sqrt(val)

    def fromPoints(P1,P2):
        pf1 = np.array(P1)
        pf2 = np.array(P2)
        return pf2-pf1

    def angle(v1,v2 = [1,0]):
        alpha =  np.arccos((np.dot(v1,v2))
                        /(vector.module(v1)*vector.module(v2)))
        if(v1[1]<v2[1]):
            alpha*=-1
        return alpha

    def fromModule(moduleDist, angle):
            return np.array([moduleDist*np.cos(angle),
                             moduleDist*np.sin(angle)])
