#GRAFICA CARTA DE PLASTICIDAD
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#linea limite liquido =50%
x=[50,50]
y=[0,60]

#linea 1
linea_1 = pd.DataFrame ({'LL':(20,100),'Ip':(0,58.4)}) #Ip = 0.73(LL-20)
#Linea 2
linea_2 = pd.DataFrame ({'LL':(8,74.666667),'Ip':(0,60)}) #Ip = 0.9(LL-8)
#Linea 3
linea_3 = pd.DataFrame ({'LL':(0,60),'Ip':(0,60)})
#lineas horizontales
#superior
linea_4 = pd.DataFrame ({'LL':(7,29.6),'Ip':(7,7)})
#inferior
linea_5 = pd.DataFrame ({'LL':(4,25.5),'Ip':(4,4)})

#imprimir formato carta de plasticidad
plt.plot(x,y,label= ' LL=50%')
plt.plot('LL','Ip',data=linea_4,linestyle='--',label='CL-ML')
plt.plot('LL','Ip',data=linea_5,linestyle='--',label='CL-ML')
plt.plot('LL','Ip',data=linea_1,linestyle='-',label='linea 1')
plt.plot('LL','Ip',data=linea_2,linestyle='-',label='linea 2')
plt.plot('LL','Ip',data=linea_3,linestyle='-',label='linea 3')
plt.legend()
plt.show()