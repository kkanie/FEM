from MS1 import czyt
from MH import M_H
from Hbc import Hbc
from Agre import Agregate
import numpy as np
from Temperatura import Temp

s = "Test1_4_4.txt"
s1 = "Test2_4_4_MixGrid.txt"
s2 = "Test3_31_31_kwadrat.txt"
s3 = "Test4_31_31_trapez.txt"
gd,  node, element, BC = czyt(s1)
# print(gd)
# print('\n')
# print(node)
# print('\n')
# print(element)
# print('\n')
# print(BC)
# print('\n')

tabx=[]
taby=[]
tabz = []
tabbc = []
# for i in node:
#     tempx, tempy=node[i]
#     tabx.append(tempx)
#     taby.append(tempy)

# print(taby)
# print(tabx)
#element
Hglo=[]
Pglo=[]
Cglo=[]
for i in range(gd['NodesNumber']):
    pom=[]
    Pglo.append(0)
    for j in range(gd['NodesNumber']):
        pom.append(0)
    Hglo.append(pom)
    Cglo.append(pom)
    

#print(Hglo[15][15])

H=[]
HBC=[]
P=[]
# print(Hglo)
# print(Cglo)
count=0
for i in element:
    print(count)
    flag1=0
    for j in range(1, 5):
        flag=0
        z=i[j]
        tempx, tempy = node[str(z)]
        tabz.append(z)
        for k in BC:
            if(z == k):
                tabbc.append(1)
                flag=1
                flag1=1
        if(flag==0):
            tabbc.append(0)
        tabx.append(tempx)
        taby.append(tempy)
    # print(taby)
    # print(tabx)
    #gd['Alfa']
    # print("-----------------------")
    # print(tabz)
    # print(tabbc)
    # # print(tabx)
    # # print(taby)
    # print("-------------------")
    Hp, C =M_H( tabx, taby, 4, gd['Conductivity'], gd['SpecificHeat'], gd['Density'] )
    # print(C)
    # print(Hp)
    HBCp, Pp = Hbc(tabx, taby, 4, tabbc, gd['Alfa'], gd['Tot'])
    HBCC=HBCp[0]
    temp = Pp[0]
    #print(temp)
    #temp = temp[0]
    #print(temp)
    #HBC.append(HBCp)
    #P.append(Pp)
    #H.append(Hp)
    # print("-----------")
    # print(Hglo)
    # print(Cglo)
    Hglo, Hfin, Pglo, Cglo = Agregate(Hglo, Hp, HBCC, temp, Pglo, Cglo, C, tabz, flag1)
    # print(Hglo)
    # print(Cglo)
    # print("-----------")
    #print(Hfin)
    #print(Hglo)
    C=[]
    Hfin=[]
    temp=[]
    tabx=[]
    taby=[]
    tabbc=[]
    tabz=[]
    Hp=[]
    Pp=[]
    HBCp=[]
    HBCC=[]
    count+=1

Cglo = np.divide(Cglo, gd['SimulationStepTime'])
t=[]
for i in range(gd['NodesNumber']):
    t.append(gd['InitialTemp'])
f = open("Temperatury\\Foo1.vtk", "w")
f.write("# vtk DataFile Version 2.0\nUnstructured Grid Example\nASCII\nDATASET UNSTRUCTURED_GRID\n\n")
f.close()
f= open("Temperatury\\Foo1.vtk", "a")
f.write("POINTS "+ str(gd['NodesNumber'])+ " float\n")
for i in range(gd['NodesNumber']):
    tempx, tempy = node[str(i+1)]
    f.write(str(tempx)+" "+str(tempy)+ " 0\n")
f.write('\n')
f.write("CELLS "+ str(gd['ElementsNumber'])+ " "+ str(gd['ElementsNumber']*5)+"\n")
for i in range(gd['ElementsNumber']):
    f.write("4 "+ str(element[i][1]-1)+" "+str(element[i][2]-1)+" "+ str(element[i][3]-1)+ " "+ str(element[i][4]-1)+"\n")
f.write("\n")
f.write("CELL_TYPES 9\n")
for i in range(gd["ElementsNumber"]):
    f.write(str(9)+"\n")
f.write('\n')
f.write("POINT_DATA "+ str(gd['NodesNumber'])+"\n")
f.write("SCALARS Temp float 1\nLOOKUP_TABLE default\n")
maks = 0
min = 1000000000000
for i in range(gd["NodesNumber"]):
    if t[i]>maks:
        maks = t[i]
    elif t[i]<min:
        min = t[i]
    f.write(str(t[i])+"\n")
f.close()
print(str(min)+" " + str(maks))

#=print(t)
for i in range(int(gd['SimulationTime']/gd['SimulationStepTime'])):
    t=Temp(Hglo, Cglo, Pglo, t)
    #print(t)
    f = open("Temperatury\\Foo%i.vtk" %(i+1), "w")
    f.write("# vtk DataFile Version 2.0\nUnstructured Grid Example\nASCII\nDATASET UNSTRUCTURED_GRID\n\n")
    f.close()
    f= open("Temperatury\\Foo%i.vtk" %(i+1), "a")
    f.write("POINTS "+ str(gd['NodesNumber'])+ " float\n")
    for i in range(gd['NodesNumber']):
        tempx, tempy = node[str(i+1)]
        f.write(str(tempx)+" "+str(tempy)+ " 0\n")
    f.write('\n')
    f.write("CELLS "+ str(gd['ElementsNumber'])+ " "+ str(gd['ElementsNumber']*5)+"\n")
    for i in range(gd['ElementsNumber']):
        f.write("4 "+ str(element[i][1]-1)+" "+str(element[i][2]-1)+" "+ str(element[i][3]-1)+ " "+ str(element[i][4]-1)+"\n")
    f.write("\n")
    f.write("CELL_TYPES "+ str(gd['ElementsNumber'])+"\n")
    for i in range(gd["ElementsNumber"]):
        f.write(str(9)+"\n")
    f.write('\n')
    f.write("POINT_DATA "+ str(gd['NodesNumber'])+"\n")
    f.write("SCALARS Temp float 1\nLOOKUP_TABLE default\n")
    maks = 0
    min = 1000000000000
    for j in range(gd["NodesNumber"]):
        if t[j]>maks:
            maks = t[j]
        elif t[j]<min:
            min = t[j]
        #print(t[j])
        f.write(str(t[j])+"\n")
    f.close()
    print(str(min)+" " + str(maks))
#print(Hglo)
#print(Pglo)
#print(Cglo)
