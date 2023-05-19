#CURVA GRANULOMETRICA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cantidad = 5
print(f"Ingresa el % tamiz pasa de los en el siguiente orden (1, 3/4, N°10, N°40,N°200):")
porcentaje_pasa = []

for i in range(cantidad):
     pasa = float(input(f"Ingrese el % pasa del tamiz: "))
     porcentaje_pasa.append(pasa)

tamiz = [37.5,25,19,9.5,4.75,2,0.85,0.425,0.25,0.15 ,0.075] 
lista_pasa = pd.Series(porcentaje_pasa)
lista_tamiz = pd.Series(tamiz)
limite_inferior = [100,84.82,55.96,36.92,24.27,16.01,10.67,7.04,4.64,3.06]
limite_superior = [100,89.6,67.91,51.46,38.90,29.48,22.49,17.05,12.92,9.79]
tamiz_limite = [25,19,9.5,4.75,2.36,1.18,0.6,0.3,0.15,0.0075]

D10=int(input("Ingrese el diametro de la malla  en mm por donde pasa el 10% del suelo "))
D30=int(input("Ingrese el diametro  de la malla en mm por donde pasa el 30% del suelo "))
D60=int(input("Ingrese el diametro  de la malla en mm por donde pasa el 60% del suelo "))

Cu_calculado=(D60/D10)
Cc_calculado=((D30**2)/D10*D60)
datos = pd.concat([lista_tamiz,lista_pasa], axis=1,keys=['APERTURA MALLA EN mm','% PASA'])

print(datos)

plt.title("CURVA GRANULOMETRICA ",fontsize=20)
plt.xlabel("TAMAÑO PARTICULA (mm)",fontsize=10)
plt.ylabel("% PASA",fontsize=10)
plt.plot(tamiz_limite,limite_inferior)
plt.plot(tamiz_limite,limite_superior)
plt.xscale("log",basex=10) 
plt.gca().invert_xaxis()
plt.show()