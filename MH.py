from MS3 import fun
import numpy as np

def M_H(tabx, taby, p, con, c, ro):
    pn, w1 = np.polynomial.legendre.leggauss(p)
    #print(pn)
    #print(w1)
    N=[]
    for i in range(p):
        for j in range(p):
            ksi=pn[j]
            eta=pn[i]
            N.append(0.25*(1-ksi)*(1-eta))
            N.append(0.25*(1+ksi)*(1-eta))
            N.append(0.25*(1+ksi)*(1+eta))
            N.append(0.25*(1-ksi)*(1+eta))
    k1, e1 = fun(p)
    dxdksi=0
    dydeta=0
    dxdeta=0
    dydksi=0
    jako = []
    Nx = []
    Ny =[]
    H = []
    C=[]
    detJ = []
    for j in range(p*p):
        
        dxdksi=0
        dydeta=0
        dxdeta=0
        dydksi=0
        for i in range(4):
            if p ==2 :
                dxdksi+=k1[i+j*4]*tabx[i]
                dydksi+=k1[i+j*4]*taby[i]
                dxdeta+=e1[i+j*4]*tabx[i]
                dydeta+=e1[i+j*4]*taby[i]
            if p >=3:
                dxdksi+=k1[i*p*p+j]*tabx[i]
                dydksi+=k1[i*p*p+j]*taby[i]
                dxdeta+=e1[i*p*p+j]*tabx[i]
                dydeta+=e1[i*p*p+j]*taby[i]
        jako.append(dxdksi)
        jako.append(dydksi)
        jako.append(dxdeta)
        jako.append(dydeta)
        detJ.append(jako[j*4+0]*jako[j*4+3]-jako[j*4+1]*jako[j*4+2])
        temp=[]
        temp.append(dydeta)
        temp.append(-dydksi)
        temp.append(-dxdeta)
        temp.append(dxdksi)
        temp=np.multiply(1/detJ[j], temp)
        for i in range(4):
            if p ==2:
                Nx.append(temp[0]*k1[i+j*4]+temp[1]*e1[i+j*4])
                Ny.append(temp[2]*k1[i+j*4]+temp[3]*e1[i+j*4])
            if p>=3:
                Nx.append(temp[0]*k1[i*p*p+j]+temp[1]*e1[i*p*p+j])
                Ny.append(temp[2]*k1[i*p*p+j]+temp[3]*e1[i*p*p+j])
        #print(Nx)
        A=[]
        B=[]
        #alfa=25
        Nc=[] 
        for k in range(4):
            for i in range(4):
                Nc.append(N[j*4+k]*N[j*4+i])
                A.append(Nx[j*4+k]*Nx[j*4+i])
                B.append(Ny[j*4+k]*Ny[j*4+i])
        #print(Nc)
        H.append(np.add(A,B)*con*detJ[j])
        ws=c*ro*detJ[j]
        C.append(np.multiply(Nc,ws))
    Hsum=[]
    Csum=[]
    if p == 2:
        Hsum = H[0]*w1[0]*w1[0]+ H[1]*w1[1]*w1[0]+H[2]*w1[0]*w1[1]+H[3]*w1[1]*w1[1]
        Csum = C[0]*w1[0]*w1[0]+ C[1]*w1[1]*w1[0]+C[2]*w1[0]*w1[1]+C[3]*w1[1]*w1[1]
    if p == 3:
        Hsum = H[0]*w1[0]*w1[0] + H[1]*w1[1]*w1[0] + H[2]*w1[2]*w1[0] +H[3]*w1[0]*w1[1] + H[4]*w1[1]*w1[1] + H[5]*w1[2]*w1[1] + H[6]*w1[0]*w1[2] + H[7]*w1[1]*w1[2] + H[8]*w1[2]*w1[2]
        Csum = C[0]*w1[0]*w1[0] + C[1]*w1[1]*w1[0] + C[2]*w1[2]*w1[0] +C[3]*w1[0]*w1[1] + C[4]*w1[1]*w1[1] + C[5]*w1[2]*w1[1] + C[6]*w1[0]*w1[2] + C[7]*w1[1]*w1[2] + C[8]*w1[2]*w1[2]
    if p ==4:
        Hsum = H[0]*w1[0]*w1[0] + H[1]*w1[1]*w1[0] + H[2]*w1[2]*w1[0] +H[3]*w1[3]*w1[0] + H[4]*w1[0]*w1[1] + H[5]*w1[1]*w1[1] + H[6]*w1[2]*w1[1] + H[7]*w1[3]*w1[1] + H[8]*w1[0]*w1[2]+ H[9]*w1[1]*w1[2] + H[10]*w1[2]*w1[2] + H[11]*w1[3]*w1[2] + H[12]*w1[0]*w1[3]  + H[13]*w1[1]*w1[3]  + H[14]*w1[2]*w1[3]  + H[15]*w1[3]*w1[3]
        Csum = C[0]*w1[0]*w1[0] + C[1]*w1[1]*w1[0] + C[2]*w1[2]*w1[0] +C[3]*w1[3]*w1[0] + C[4]*w1[0]*w1[1] + C[5]*w1[1]*w1[1] + C[6]*w1[2]*w1[1] + C[7]*w1[3]*w1[1] + C[8]*w1[0]*w1[2]+ C[9]*w1[1]*w1[2] + C[10]*w1[2]*w1[2] + C[11]*w1[3]*w1[2] + C[12]*w1[0]*w1[3]  + C[13]*w1[1]*w1[3]  + C[14]*w1[2]*w1[3]  + C[15]*w1[3]*w1[3]
       
    return Hsum, Csum
    

# tx =[0, 0.025, 0.025, 0]
# ty = [0, 0, 0.025, 0.025]
# p=3
# c=700
# ro=7800
# print(M_H(tx, ty, p, 30, c, ro))
