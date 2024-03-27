import numpy as np


# tabx = [0, 0.025, 0.025, 0]
# taby = [0, 0, 0.025, 0.025]

#Bc=[1, 1, 1, 1]

def Hbc(tabx, taby, p, BC, con, tot):
    tab, w1 = np.polynomial.legendre.leggauss(p)
    #con=25
    detj=[]
    pom=[]
    N=[]
    Hb=[]
    P=[]
    HBC=[]
    Pk=[]

    detj.append(pow((pow(tabx[3]-tabx[0], 2) + pow(taby[3]-taby[0], 2)),0.5)/2)
    for i in range(3, 0, -1):
        detj.append(pow((pow(tabx[i]-tabx[i-1], 2) + pow(taby[i]-taby[i-1], 2)),0.5)/2)

    #print(detj)

    for r in range(4):
        
        Hbcc=[]
        Pmm=[]
       
        N=[]
        for i in range(p):
            if r == 0:
                ksi = -1
                eta = tab[i]
            elif r == 1:
                ksi = tab[i]
                eta = 1
            elif r == 2:
                ksi = 1
                eta = tab[i]
            else:
                ksi = tab[i]
                eta = -1
            N.append(0.25*(1-ksi)*(1-eta))
            N.append(0.25*(1+ksi)*(1-eta))
            N.append(0.25*(1+ksi)*(1+eta))
            N.append(0.25*(1-ksi)*(1+eta))

        # print("TO JEST N -----------")
        # print(N)

        for k in range(p):
            pom = []
            for i in range(4):
                for j in range(4):
                    zm = (N[i+k*4]*N[j+k*4]) * con * w1[k] * detj[r]
                    pom.append(zm)
            if k == 0:
                Hbcc.append(pom)
            else:
                Hbcc=np.add(Hbcc, pom)
        for k in range(p):
            Pm=[]
            for i in range(4):
                pm = (N[i+k*4]*tot) * con * w1[k] * detj[r]
                Pm.append(pm)
            if k == 0:
                Pmm.append(Pm)
            else:
                Pmm=np.add(Pmm, Pm)
        P.append(Pmm)
        #print("TO JEST Hbcc -----------")
        #print(Hbcc)
        Hb.append(Hbcc)
    # for i in range(len(Hb)):
    #     print("HB____---------------")
    #     print(Hb[i])
    #     print("P____---------------")
    #     print(P[i])
    # print("KONIEC-----------------------")
    for i in range(4):
        Pk.append(0)
        for j in range(4):
            HBC.append(0)
    if(BC[0]==1 and BC[1]==1):
        # print(tabx[0])
        # print(taby[0])
        # print(tabx[1])
        # print(taby[1])
        HBC=np.add(HBC, Hb[3])
        Pk=np.add(Pk, P[3])
    if(BC[1]==1 and BC[2]==1):
        # print(tabx[1])
        # print(taby[1])
        # print(tabx[2])
        # print(taby[2])
        HBC=np.add(HBC, Hb[2])
        Pk=np.add(Pk, P[2])
    if(BC[2]==1 and BC[3]==1):
        # print(tabx[2])
        # print(taby[2])
        # print(tabx[3])
        # print(taby[3])
        HBC=np.add(HBC, Hb[1])
        Pk=np.add(Pk, P[1])
    if(BC[0]==1 and BC[3]==1):
        # print(tabx[0])
        # print(taby[0])
        # print(tabx[3])
        # print(taby[3])
        HBC=np.add(HBC, Hb[0])
        Pk=np.add(Pk, P[0])
    
    return(HBC, Pk)
    



#Hbc(2, Bc)
                    
                





        
