
import numpy as np

def N(x):
    return 0.25 * (1-x)

def N1(x):
    return 0.25 * (1-x)

tab = [pow(1/3,0.5), 0 ,pow(3/5,0.5), pow((3/7)-(2/7)*pow(6/5,0.5),0.5),  pow((3/7)+(2/7)*pow(6/5,0.5),0.5)]

tab4, w1 = np.polynomial.legendre.leggauss(4)

def fun(p):
    tab_ksi = []
    tab_eta = []
    if p==2:
        for i in range(2):#funkcje ksztłu
            for j in range(2):#punkty całkowania
                if i <1:
                    tab_ksi.append(-N(-tab[0]))
                    tab_ksi.append(N(-tab[0]))
                    tab_ksi.append(N(tab[0]))
                    tab_ksi.append(-N(tab[0]))

                    if j == 0: 
                        tab_eta.append(-N(-tab[0]))
                        tab_eta.append(-N(tab[0]))
                        tab_eta.append(N(tab[0]))
                        tab_eta.append(N(-tab[0]))
                    if j == 1:
                        tab_eta.append(-N(tab[0]))
                        tab_eta.append(-N(-tab[0]))
                        tab_eta.append(N(-tab[0]))
                        tab_eta.append(N(tab[0]))
                    
                else:
                    tab_ksi.append(-N(tab[0]))
                    tab_ksi.append(N(tab[0]))
                    tab_ksi.append(N(-tab[0]))
                    tab_ksi.append(-N(-tab[0]))
                    if j == 0:
                        tab_eta.append(-N(-tab[0]))
                        tab_eta.append(-N(tab[0]))
                        tab_eta.append(N(tab[0]))
                        tab_eta.append(N(-tab[0]))

                        
                    else:
                        tab_eta.append(-N(tab[0]))
                        tab_eta.append(-N(-tab[0]))
                        tab_eta.append(N(-tab[0]))
                        tab_eta.append(N(tab[0]))
    if p == 3:
        k=1
        c = 2
        for i in range(4):#funkcje ksztłu
            for j in range(3):#punkty całkowania
                if i == 0:
                    tab_ksi.append(-N1(-tab[2]))
                    tab_ksi.append(-N1(tab[1]))
                    tab_ksi.append(-N1(tab[2]))
                    if j == 2:
                        k=-1
                    else:
                        k=1
                    if j ==1:
                        c = 1
                    else:
                        c = 2
                    tab_eta.append(-N(k*(-tab[c])))
                    tab_eta.append(-N(k*(-tab[c])))
                    tab_eta.append(-N(k*(-tab[c])))
                elif i == 1:
                    tab_ksi.append(-N1(tab[2]))
                    tab_ksi.append(-N1(tab[1]))
                    tab_ksi.append(-N1(-tab[2]))
                    if j == 2:
                        k=-1
                    else:
                        k=1
                    if j ==1:
                        c = 1
                    else:
                        c = 2
                    tab_eta.append(N(k*(-tab[c])))
                    tab_eta.append(N(k*(-tab[c])))
                    tab_eta.append(N(k*(-tab[c])))
                    
                elif i == 2:
                     tab_ksi.append(N1(tab[2]))
                     tab_ksi.append(N1(tab[1]))
                     tab_ksi.append(N1(-tab[2]))
                     if j == 2:
                        k=1
                     else:
                        k=-1
                     if j ==1:
                        c = 1
                     else:
                        c = 2
                     tab_eta.append(N(k*(-tab[c])))
                     tab_eta.append(N(k*(-tab[c])))
                     tab_eta.append(N(k*(-tab[c])))
                elif i == 3:
                    tab_ksi.append(N1(-tab[2]))
                    tab_ksi.append(N1(tab[1]))
                    tab_ksi.append(N1(tab[2]))
                    if j == 2:
                        k=1
                    else:
                        k=-1
                    if j ==1:
                        c = 1
                    else:
                        c = 2
                    tab_eta.append(-N(k*(-tab[c])))
                    tab_eta.append(-N(k*(-tab[c])))
                    tab_eta.append(-N(k*(-tab[c])))
        return tab_eta, tab_ksi
    if p == 4:
        k=1
        c = 4
        for i in range(4):#funkcje ksztłu
            for j in range(4):#punkty całkowania
                if i == 0:
                    tab_ksi.append(-N1(tab4[j]))
                    tab_ksi.append(-N1(tab4[j]))
                    tab_ksi.append(-N1(tab4[j]))
                    tab_ksi.append(-N1(tab4[j]))
                    tab_eta.append(-N((tab4[0])))
                    tab_eta.append(-N((tab4[1])))
                    tab_eta.append(-N((tab4[2])))
                    tab_eta.append(-N((tab4[3])))
                elif i == 1:
                    tab_ksi.append(N1(tab4[j]))
                    tab_ksi.append(N1(tab4[j]))
                    tab_ksi.append(N1(tab4[j]))
                    tab_ksi.append(N1(tab4[j]))
                    tab_eta.append(-N(-(tab4[0])))
                    tab_eta.append(-N(-(tab4[1])))
                    tab_eta.append(-N(-(tab4[2])))
                    tab_eta.append(-N(-(tab4[3])))
                elif i == 2:
                    tab_ksi.append(N1(-tab4[j]))
                    tab_ksi.append(N1(-tab4[j]))
                    tab_ksi.append(N1(-tab4[j]))
                    tab_ksi.append(N1(-tab4[j]))
                    tab_eta.append(N(-(tab4[0])))
                    tab_eta.append(N(-(tab4[1])))
                    tab_eta.append(N(-(tab4[2])))
                    tab_eta.append(N(-(tab4[3])))
                elif i == 3:
                    tab_ksi.append(-N1(-tab4[j]))
                    tab_ksi.append(-N1(-tab4[j]))
                    tab_ksi.append(-N1(-tab4[j]))
                    tab_ksi.append(-N1(-tab4[j]))
                    tab_eta.append(N((tab4[0])))
                    tab_eta.append(N((tab4[1])))
                    tab_eta.append(N((tab4[2])))
                    tab_eta.append(N((tab4[3])))


    return  tab_ksi, tab_eta

# k, e = fun(4)
# print(np.matrix(k))
# print(np.matrix(e))
        

