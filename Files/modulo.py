# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:15:07 2020

@author: Jader Peñaloza
"""

import numpy as np
import pandas as pd

def activacion(x):
    
    acti= 1
    
    if x>=0:
        acti=1
    elif x<0:
        acti=-1
    return acti

def cargar_datos(ruta):
    
    datos= pd.read_csv(ruta,delimiter=";")
    
    
    return datos

def iteracion(W,U,datos,rata=0.1, X0=1):
    
    cargados= cargar_datos(datos)
    
    X1= cargados["X1"]
    
    X2= cargados["X2"]
    
    Yd1= cargados["Yd1"]
    
    Yr1= np.array([])
    
    EP=np.array([])
    
    Eli=np.array([])

    Si=np.array([])
    
    for i in range(len(X1)):
        
        Si=np.append(Si,((X1[i]*W[0])+(X2[i]*W[1]))-U)
        
        Yr1= np.append(Yr1,activacion(Si[i]))
        
        Eli=np.append(Eli,Yd1[i]-Yr1[i])
        
        EP= np.append(EP,abs(Eli[i]))
        
        W[0]=W[0]+(rata*Eli[i]*X1[i])
        
        W[1]=W[1]+(rata*Eli[i]*X2[i])
        
        U= U +(rata*Eli[i]*X0)
        
        
    
    Erms=np.sum(EP)/len(EP)
    
    return W,U,Erms,Yr1,Yd1
    

def init(datos,rata=0.1, X0=1):
    
    
    cargados= cargar_datos(datos)
    
    U= cargados["U"][0]
    
    W= np.array([cargados["W"][0],cargados["W"][1]])
    
    X1= cargados["X1"]
    
    X2= cargados["X2"]
    
    Yd1= cargados["Yd1"]
    
    Yr1= np.array([])
    
    EP=np.array([])
    
    Eli=np.array([])

    Si=np.array([])
    
    for i in range(len(X1)):
        
        Si=np.append(Si,((X1[i]*W[0])+(X2[i]*W[1]))-U)
        
        Yr1= np.append(Yr1,activacion(Si[i]))
        
        Eli=np.append(Eli,Yd1[i]-Yr1[i])
        
        EP= np.append(EP,abs(Eli[i]))
        
        W[0]=W[0]+(rata*Eli[i]*X1[i])
        
        W[1]=W[1]+(rata*Eli[i]*X2[i])
        
        U= U +(rata*Eli[i]*X0)
        
        
    
    Erms=np.sum(EP)/len(EP)
    
    return W,U,Erms,Yr1,Yd1


def modelo(error_max,datos):
    
    W,U,Erms,Yr1,Yd1= init(datos=datos)
    
    
    
    iteraciones= 1

    
    while error_max< Erms:
        
        W,U,Erms,Yr1,Yd1=iteracion(W,U,datos,rata=0.1, X0=1)
        
        iteraciones=iteraciones+1
        if iteraciones ==100:

            break;        
    
    return W,U

def probar_valor(W,U,X1,X2):
    
    Si=((X1*W[0])+(X2*W[1]))-U
    
    Yd1=activacion(Si)
    
    return Yd1