import numpy as np

def Temp(H, C, P, t):
    L = np.add(H,C)
    Pp = np.dot(C,t)
    Pp = np.add(Pp, P)
    X = np.linalg.solve(L,Pp)
    return X