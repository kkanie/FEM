import numpy as np
import copy

def Agregate(Hglo, H, Hbc, P, Pglo, Cglo, C, tabz, flag1):
    Hfin=[]
    Cfin=[]
    Cglo_copy = copy.deepcopy(Cglo)
    for i in range(4):
        hpom=[]
        cpom=[]
        for j in range(4):
            hpom.append(H[i*4+j])
            cpom.append(C[i*4+j])
        Hfin.append(hpom)
        Cfin.append(cpom)
    #Hfin=H
    pomhbc=[]
    if(flag1==1):
        for i in range(4):
            pim=[]
            for j in range(4):
                pim.append(Hbc[4*i+j])
            pomhbc.append(pim)
        Hfin=np.add(Hfin, pomhbc)
    Hfin_copy = copy.deepcopy(Hfin)
    Cfin_copy = copy.deepcopy(Cfin)
    for i in range(len(tabz)):
        for j in range(len(tabz)):
            Hglo[tabz[i]-1][tabz[j]-1] += Hfin_copy[i][j]
            Cglo_copy[tabz[i]-1][tabz[j]-1] += Cfin_copy[i][j]
        if flag1 == 1:
            Pglo[tabz[i]-1]+=P[i]
    
    return Hglo, Hfin_copy, Pglo, Cglo_copy

