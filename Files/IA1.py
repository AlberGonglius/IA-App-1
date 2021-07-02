import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import sqlite3
import modulo
class Neurona:
    def __init__(self,window):
        self.wind=window
        self.wind.title("Perceptron unicapa Bipolar, JADER PEÑALOZA")
        
        self.nombre_archivo=""
        self.iteraciones=0
        self.parar= False
        self.set_default()
        
        
        
        
        #Fondo
        background=Image.open("fondo gris.png")
        background=background.resize((window.winfo_screenwidth(),window.winfo_screenheight()),Image.ANTIALIAS)
        bk_photo = ImageTk.PhotoImage(background)
        
        bk_label=tk.Label(self.wind,image=bk_photo)
        bk_label.image=bk_photo
        bk_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        #Titulo
        
        titulo= Label(self.wind,text="Perceptrón Unicapa Bipolar",font=("Arial",26))
        titulo.place(x=window.winfo_screenwidth()/3,y=window.winfo_screenheight()/20)
        
        #Iteraciones
        
        self.IMG1_SIZE_HEIGHT=round(window.winfo_screenheight()/1.5)
        IMG1_SIZE_HEIGHT=round(window.winfo_screenheight()/1.5)
        
        img1=Image.open("img1.png")
        img1=img1.resize((round(window.winfo_screenwidth()/4),IMG1_SIZE_HEIGHT))
        img1_photo = ImageTk.PhotoImage(img1)
        
        img1_label= tk.Label(self.wind,image=img1_photo)
        img1_label.image=img1_photo
        img1_label.place(x=0,y=(window.winfo_screenheight()/8))
        
        
        ## ITE1
        self.ite1=Image.open("ite1.png")
        self.ite1=self.ite1.resize((round(window.winfo_screenwidth()/8),round(IMG1_SIZE_HEIGHT/6)))
        self.ite1 = ImageTk.PhotoImage(self.ite1)
        self.ite1_label= tk.Label(self.wind,image=self.ite1)
        self.ite1_label.image=self.ite1
        self.ite1_label.place(x=round(window.winfo_screenwidth()/4)+10,y=(window.winfo_screenheight()/8))
        ## ITE2
        self.ite2=Image.open("ite2.png")
        self.ite2=self.ite2.resize((round(window.winfo_screenwidth()/8),round(IMG1_SIZE_HEIGHT/6)))
        self.ite2 = ImageTk.PhotoImage(self.ite2)
        self.ite2_label= tk.Label(self.wind,image=self.ite2)
        self.ite2_label.image=self.ite2
        self.ite2_label.place(x=round(window.winfo_screenwidth()/4)+10,y=(window.winfo_screenheight()/8)+IMG1_SIZE_HEIGHT/6)
        ## ITE3
        self.ite3=Image.open("ite3.png")
        self.ite3=self.ite3.resize((round(window.winfo_screenwidth()/8),round(IMG1_SIZE_HEIGHT/6)))
        self.ite3 = ImageTk.PhotoImage(self.ite3)
        self.ite3_label= tk.Label(self.wind,image=self.ite3)
        self.ite3_label.image=self.ite3
        self.ite3_label.place(x=round(window.winfo_screenwidth()/4)+10,y=(window.winfo_screenheight()/8)+(2*IMG1_SIZE_HEIGHT/6))
        ## ITE4
        self.ite4=Image.open("ite4.png")
        self.ite4=self.ite4.resize((round(window.winfo_screenwidth()/8),round(IMG1_SIZE_HEIGHT/6)))
        self.ite4 = ImageTk.PhotoImage(self.ite4)
        self.ite4_label= tk.Label(self.wind,image=self.ite4)
        self.ite4_label.image=self.ite4
        self.ite4_label.place(x=round(window.winfo_screenwidth()/4)+10,y=(window.winfo_screenheight()/8)+(3*IMG1_SIZE_HEIGHT/6))
        ## ITE5
        self.ite5=Image.open("ite5.png")
        self.ite5=self.ite5.resize((round(window.winfo_screenwidth()/8),round(IMG1_SIZE_HEIGHT/6)))
        self.ite5 = ImageTk.PhotoImage(self.ite5)
        self.ite5_label= tk.Label(self.wind,image=self.ite5)
        self.ite5_label.image=self.ite5
        self.ite5_label.place(x=round(window.winfo_screenwidth()/4)+10,y=(window.winfo_screenheight()/8)+(4*IMG1_SIZE_HEIGHT/6))
        ## ITE6
        self.ite6=Image.open("ite6.png")
        self.ite6=self.ite6.resize((round(window.winfo_screenwidth()/8),round(IMG1_SIZE_HEIGHT/6)))
        self.ite6 = ImageTk.PhotoImage(self.ite6)
        self.ite6_label= tk.Label(self.wind,image=self.ite6)
        self.ite6_label.image=self.ite6
        self.ite6_label.place(x=round(window.winfo_screenwidth()/4)+10,y=(window.winfo_screenheight()/8)+(5*IMG1_SIZE_HEIGHT/6))
        
        #Flecha
        img1=Image.open("flecha.png")
        img1=img1.resize((round(window.winfo_screenwidth()/18),round(IMG1_SIZE_HEIGHT/6)))
        img1_photo = ImageTk.PhotoImage(img1)
        
        img1_label= tk.Label(self.wind,image=img1_photo)
        img1_label.image=img1_photo
        img1_label.place(x=round(window.winfo_screenwidth()/4)+20+round(window.winfo_screenwidth()/8),
                         y=((window.winfo_screenheight()/8)+IMG1_SIZE_HEIGHT)/2)
        
        
        posx_actual=round(window.winfo_screenwidth()/4)+20+round(window.winfo_screenwidth()/8)+round(window.winfo_screenwidth()/18)
        posy_actual=((window.winfo_screenheight()/8)+IMG1_SIZE_HEIGHT)/2
        
        ## todas las iteraciones
        self.allite=Image.open("allite.png")
        self.allite=self.allite.resize((round(window.winfo_screenwidth()/6),round(window.winfo_screenheight()/4)))
        self.allite = ImageTk.PhotoImage(self.allite)
        self.allite_label= tk.Label(self.wind,image=self.allite)
        self.allite_label.image=self.allite
        self.allite_label.place(x=posx_actual+10,y=(window.winfo_screenheight()/8)+(1.7*IMG1_SIZE_HEIGHT/6))
        
        posx_actual=posx_actual+round(window.winfo_screenwidth()/6)
        posy_actual=(window.winfo_screenheight()/8)+(1.7*IMG1_SIZE_HEIGHT/6)
        #Flecha2
        img1=Image.open("flecha.png")
        img1=img1.resize((round(window.winfo_screenwidth()/18),round(IMG1_SIZE_HEIGHT/6)))
        img1_photo = ImageTk.PhotoImage(img1)
        
        img1_label= tk.Label(self.wind,image=img1_photo)
        img1_label.image=img1_photo
        img1_label.place(x=posx_actual+20,y=((window.winfo_screenheight()/8)+IMG1_SIZE_HEIGHT)/2)
        
        
        #Neurona 
        img1=Image.open("neurona.png")
        img1=img1.resize((round(window.winfo_screenwidth()/18),round(IMG1_SIZE_HEIGHT/6)))
        img1_photo = ImageTk.PhotoImage(img1)
        
        img1_label= tk.Label(self.wind,image=img1_photo)
        img1_label.image=img1_photo
        img1_label.place(x=posx_actual+round(window.winfo_screenwidth()/18)+30,y=((window.winfo_screenheight()/8)+IMG1_SIZE_HEIGHT)/2)
        
        
        posx_actual=posx_actual+round(window.winfo_screenwidth()/18)+30+round(window.winfo_screenwidth()/18)
        #Grafica entrenada
        self.graf_entrenada=Image.open("entrenada.png")
        self.graf_entrenada=self.graf_entrenada.resize((round(window.winfo_screenwidth()/4.5),round(window.winfo_screenheight()/3)))
        self.graf_entrenada = ImageTk.PhotoImage(self.graf_entrenada)
        
        self.graf_entrenada_label= tk.Label(self.wind,image=self.graf_entrenada)
        self.graf_entrenada_label.image=self.graf_entrenada
        self.graf_entrenada_label.place(x=posx_actual+10,y=window.winfo_screenheight()/4)
        
        
        #Datos
        
        rata_aprendizaje=Label(self.wind,text = "Rata de Aprendizaje",font=("Helvetica", 10))
        rata_aprendizaje.place(x=(1.5*window.winfo_screenwidth()/3),y=1.9*window.winfo_screenheight()/3)
        self.rata_aprendizaje=Entry(self.wind,font=("Arial", 10))
        self.rata_aprendizaje.place(x=(1.8*window.winfo_screenwidth()/3),y=1.9*window.winfo_screenheight()/3)
        
        error=Label(self.wind,text = "Error",font=("Helvetica", 10))
        error.place(x=(1.5*window.winfo_screenwidth()/3),y=2.1*window.winfo_screenheight()/3)
        self.error=Entry(self.wind,font=("Arial", 10))
        self.error.place(x=(1.8*window.winfo_screenwidth()/3),y=2.1*window.winfo_screenheight()/3)
        
        error_max=Label(self.wind,text = "Error Max Permitido",font=("Helvetica", 10))
        error_max.place(x=(1.5*window.winfo_screenwidth()/3),y=2*window.winfo_screenheight()/3)
        self.error_max=Entry(self.wind,font=("Arial", 10))
        self.error_max.place(x=(1.8*window.winfo_screenwidth()/3),y=2*window.winfo_screenheight()/3)
                        
        ite=Label(self.wind,text = "iteraciones",font=("Helvetica", 10))
        ite.place(x=(1.5*window.winfo_screenwidth()/3),y=2.2*window.winfo_screenheight()/3)
        self.ite=Entry(self.wind,font=("Arial", 10))
        self.ite.place(x=(1.8*window.winfo_screenwidth()/3),y=2.2*window.winfo_screenheight()/3)  
        self.ite.insert(0,str(self.iteraciones))
        
        
        # Probar
        x1=Label(self.wind,text = "X1",font=("Helvetica", 10))
        x1.place(x=(2.3*window.winfo_screenwidth()/3),y=1.9*window.winfo_screenheight()/3)
        self.x1=Entry(self.wind,font=("Arial", 10))
        self.x1.place(x=(2.4*window.winfo_screenwidth()/3),y=1.9*window.winfo_screenheight()/3)
        
        x2=Label(self.wind,text = "X2",font=("Helvetica", 10))
        x2.place(x=(2.3*window.winfo_screenwidth()/3),y=2*window.winfo_screenheight()/3)
        self.x2=Entry(self.wind,font=("Arial", 10))
        self.x2.place(x=(2.4*window.winfo_screenwidth()/3),y=2*window.winfo_screenheight()/3)
        
        y1=Label(self.wind,text = "Yd1",font=("Helvetica", 10))
        y1.place(x=(2.3*window.winfo_screenwidth()/3),y=2.2*window.winfo_screenheight()/3)
        self.y1=Entry(self.wind,font=("Arial", 10))
        self.y1.place(x=(2.4*window.winfo_screenwidth()/3),y=2.2*window.winfo_screenheight()/3)
        
        #BOTONES
        button_abri=Button(self.wind,text="Abrir",font=("Helveltica",18),command=self.abrir)
        button_abri.place(x=(1.5*window.winfo_screenwidth()/3),y=4*window.winfo_screenheight()/5)
        
        button_init=Button(self.wind,text="Inicializar",font=("Helveltica",18),command=self.inicializar)
        button_init.place(x=(1.7*window.winfo_screenwidth()/3),y=4*window.winfo_screenheight()/5)
        
        button_entr=Button(self.wind,text="Entrenar",font=("Helveltica",18),command=self.entrenar)
        button_entr.place(x=(2.01*window.winfo_screenwidth()/3),y=4*window.winfo_screenheight()/5)
        
        button_parar=Button(self.wind,text="Parar",font=("Helveltica",18),command=self.parar_ent)
        button_parar.place(x=(2.3*window.winfo_screenwidth()/3),y=4*window.winfo_screenheight()/5)
        
        button_probar=Button(self.wind,text="Probar",font=("Helveltica",18), command=self.probar)
        button_probar.place(x=(2.5*window.winfo_screenwidth()/3),y=4*window.winfo_screenheight()/5)
        
        button_salir=Button(self.wind,text="Salir",font=("Helveltica",18),command=self.salir)
        button_salir.place(x=(2.8*window.winfo_screenwidth()/3),y=4*window.winfo_screenheight()/5)
    
    def actualizar(self):
        self.ite1=Image.open("ite1.png")
        self.ite1=self.ite1.resize((round(self.wind.winfo_screenwidth()/8),round(self.IMG1_SIZE_HEIGHT/6)))
        self.ite1 = ImageTk.PhotoImage(self.ite1)
        self.ite1_label.configure(image=self.ite1)
        self.ite1_label.image=self.ite1
        
        self.ite2=Image.open("ite2.png")
        self.ite2=self.ite2.resize((round(self.wind.winfo_screenwidth()/8),round(self.IMG1_SIZE_HEIGHT/6)))
        self.ite2 = ImageTk.PhotoImage(self.ite2)
        self.ite2_label.configure(image=self.ite2)
        self.ite2_label.image=self.ite2
        
        self.ite3=Image.open("ite3.png")
        self.ite3=self.ite3.resize((round(self.wind.winfo_screenwidth()/8),round(self.IMG1_SIZE_HEIGHT/6)))
        self.ite3 = ImageTk.PhotoImage(self.ite3)
        self.ite3_label.configure(image=self.ite3)
        self.ite3_label.image=self.ite3
        
        self.ite4=Image.open("ite4.png")
        self.ite4=self.ite4.resize((round(self.wind.winfo_screenwidth()/8),round(self.IMG1_SIZE_HEIGHT/6)))
        self.ite4 = ImageTk.PhotoImage(self.ite4)
        self.ite4_label.configure(image=self.ite4)
        self.ite4_label.image=self.ite4
        
        self.ite5=Image.open("ite5.png")
        self.ite5=self.ite5.resize((round(self.wind.winfo_screenwidth()/8),round(self.IMG1_SIZE_HEIGHT/6)))
        self.ite5 = ImageTk.PhotoImage(self.ite5)
        self.ite5_label.configure(image=self.ite5)
        self.ite5_label.image=self.ite5
        
        self.ite6=Image.open("ite6.png")
        self.ite6=self.ite6.resize((round(self.wind.winfo_screenwidth()/8),round(self.IMG1_SIZE_HEIGHT/6)))
        self.ite6 = ImageTk.PhotoImage(self.ite6)
        self.ite6_label.configure(image=self.ite6)
        self.ite6_label.image=self.ite6
        
        self.allite=Image.open("allite.png")
        self.allite=self.allite.resize((round(self.wind.winfo_screenwidth()/6),round(self.wind.winfo_screenheight()/4)))
        self.allite = ImageTk.PhotoImage(self.allite)
        self.allite_label.configure(image=self.allite)
        self.allite_label.image=self.allite
        
        self.graf_entrenada=Image.open("entrenada.png")
        self.graf_entrenada=self.graf_entrenada.resize((round(self.wind.winfo_screenwidth()/4.5),round(self.wind.winfo_screenheight()/3)))
        self.graf_entrenada = ImageTk.PhotoImage(self.graf_entrenada)
        self.graf_entrenada_label.configure(image=self.graf_entrenada)
        self.graf_entrenada_label.image=self.graf_entrenada
        
        self.ite.delete(0,'end')
        self.ite.insert(0,str(self.iteraciones))
        
    
    def set_default(self):
        
        for i in range(6):
            plt.plot([0],[0])
            plt.savefig("ite"+str(i+1)+".png")
        for i in range(6):
            plt.plot([0],[0])
        plt.savefig("allite.png")
        plt.savefig("entrenada.png")
        self.iteraciones=0
        
    def salir(self):
        self.iteraciones=0
        self.parar=False
        self.set_default()
        self.actualizar()
        self.wind.destroy()
        
    def abrir(self,event=None):
        self.nombre_archivo = filedialog.askopenfilename()
        
    def graficar_init(self,Yr1,Yd1):
        
        for i in range(len(Yr1)):
            plt.plot([0,Yd1[i]],[0,Yr1[i]])
            plt.axvline(color='k',linewidth=.8)
            plt.axhline(color='k',linewidth=.8)
            plt.title('Yd1 vs Yr1'" ite"+str(i+1),Fontsize=22)
            plt.ylabel('Yr1',Fontsize=15)
            plt.xlabel('Yd1', Fontsize=15)
            plt.grid()
            plt.savefig("ite"+str(i+1)+".png")
            plt.close('all')
            
        for i in range(len(Yr1)):
            plt.plot([0,Yd1[i]],[0,Yr1[i]])
        plt.axvline(color='k',linewidth=.8)
        plt.axhline(color='k',linewidth=.8)
        plt.title('Yd1 vs Yr1',Fontsize=20)
        plt.grid()
        plt.savefig("allite.png")
        plt.close('all')
        
        plt.plot(Yd1,Yr1,"g*")
        plt.plot(Yd1,Yr1,"r-")
        plt.axvline(color='k',linewidth=.8)
        plt.axhline(color='k',linewidth=.8)
        plt.title('Yd1 vs Yr1 Entrenada',Fontsize=20)
        plt.grid()
        plt.savefig("entrenada.png")
        plt.close('all')
        plt.cla()
        plt.clf()

    
    def parar_ent(self):
        
        self.parar=True
        
    def entrenar(self):

        self.W,self.U,Erms,Yr1,Yd1=modulo.init(self.nombre_archivo)
        
        self.iteraciones=1
        
        while float(self.error_max.get()) < Erms and self.parar== False:

            self.W,self.U,Erms,Yr1,Yd1=modulo.iteracion(self.W,self.U,self.nombre_archivo,rata=float(self.rata_aprendizaje.get()), X0=1)
            self.error.delete(0,'end') 
            self.error.insert(0,str(Erms))
            self.iteraciones=self.iteraciones+1
            self.graficar_init(Yr1,Yd1)
            self.actualizar()
    def probar(self):
        
        yd1=modulo.probar_valor(self.W,self.U,float(self.x1.get()),float(self.x2.get()))
        
        self.y1.delete(0,'end')
        self.y1.insert(0,str(yd1))
        
    def inicializar(self):
        
        self.W,self.U,Erms,Yr1,Yd1=modulo.init(self.nombre_archivo,rata=float(self.rata_aprendizaje.get()))
        self.error.delete(0,'end')
        self.error.insert(0,str(Erms))
        
        self.iteraciones=1
        
        
        self.graficar_init(Yr1,Yd1)
        
        self.y1.delete(0,'end')
        self.x1.delete(0,'end')
        self.x2.delete(0,'end')
        self.actualizar()
             
if __name__== "__main__":
    window= Tk()
    window.geometry("%dx%d+0+0"%(window.winfo_screenwidth(),window.winfo_screenheight()))
    application=Neurona(window)
    window.mainloop()




