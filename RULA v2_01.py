import tkinter as tk
from tkinter import StringVar, ttk

######################################################
def focus_next_window(event):
    event.widget.tk_focusNext().focus()

def focus_prev_window(event):
    event.widget.tk_focusPrev().focus()
######################################################

#Defino las funciones que luego voy a usar
def limpiarCampos(event):
    allFields = [nu1, 
                nu2, 
                nu3, 
                nu4, 
                nu5, 
                nu6, 
                nu11, 
                nu12, 
                nu13, 
                nu14, 
                nu15, 
                nu16, 
                nu21, 
                nu22, 
                nu23, 
                nu24, 
                nu25,
                nu26]                
    for i in allFields:
        i.delete(0, tk.END)
        #i.insert(tk.END, 0)

        # borro 4 filas inferiores de los Resultados 
        f = ("Arial",14, "bold")
        tk.Label(text="     ",font=f).grid(row=7, column=1)
        tk.Label(text="       ",font=f).grid(row=8, column=1)
        tk.Label(text="       ",font=f).grid(row=9, column=1)
        tk.Label(text="       ",font=f).grid(row=10, column=1)
        
        tk.Label(text="     ",font=f).grid(row=7, column=2)
        tk.Label(text="       ",font=f).grid(row=8, column=2)
        tk.Label(text="       ",font=f).grid(row=9, column=2)
        tk.Label(text="       ",font=f).grid(row=10, column=2)

        tk.Label(text="     ",font=f).grid(row=7, column=3)
        tk.Label(text="       ",font=f).grid(row=8, column=3)
        tk.Label(text="       ",font=f).grid(row=9, column=3)
        tk.Label(text="       ",font=f).grid(row=10, column=3)

def validaYSuma(event):
# Validacion
    # Column 1
        try:
            numero1 = int(nu1.get())
        except:
            numero1 = 0

        try:
            numero2 = int(nu2.get())
        except:
            numero2 = 0   

        try:
            numero3 = int(nu3.get())
        except:
            numero3 = 0

        try:
            numero4 = int(nu4.get())
        except:
            numero4 = 0  

        try:
            numero5 = int(nu5.get())
        except:
            numero5 = 0

        try:
            numero6 = int(nu6.get())
        except:
            numero6 = 0  

    # Column 2
        try:
            numero11 = int(nu11.get())
        except:
            numero11 = 0

        try:
            numero12 = int(nu12.get())
        except:
            numero12 = 0   

        try:
            numero13 = int(nu13.get())
        except:
            numero13 = 0

        try:
            numero14 = int(nu14.get())
        except:
            numero14 = 0  

        try:
            numero15 = int(nu15.get())
        except:
            numero15 = 0

        try:
            numero16 = int(nu16.get())
        except:
            numero16 = 0  

    # Column 3
        try:
            numero21 = int(nu21.get())
        except:
            numero21 = 0

        try:
            numero22 = int(nu22.get())
        except:
            numero22 = 0   

        try:
            numero23 = int(nu23.get())
        except:
            numero23 = 0

        try:
            numero24 = int(nu24.get())
        except:
            numero24 = 0  

        try:
            numero25 = int(nu25.get())
        except:
            numero25 = 0

        try:
            numero26 = int(nu26.get())
        except:
            numero26 = 0  
        

# Suma
        f = ("Arial",13, "bold")

        res = (numero1*35) + (numero2*17) +( numero3*8) + (numero4*11) + (numero5*5)
        res2= res-numero6
      
        tk.Label(text=res,font=f,fg="Black").grid(row=7, column=1)
        tk.Label(text=res2*10,font=f,fg="Blue").grid(row=8, column=1)
        tk.Label(text=res2*25,font=f,fg="green").grid(row=9, column=1)
        tk.Label(text=res2*50,font=f,fg="Black").grid(row=10, column=1)

        res3 = (numero11*35) + (numero12*17) +( numero13*8) + (numero14*11) + (numero15*5)
        res4= res3-numero16
        tk.Label(text=res3,font=f,fg="Black").grid(row=7, column=2)
        tk.Label(text=res4*10,font=f,fg="Blue").grid(row=8, column=2)
        tk.Label(text=res4*25,font=f,fg="green").grid(row=9, column=2)
        tk.Label(text=res4*50,font=f,fg="Black").grid(row=10, column=2)

        res5 = (numero21*35) + (numero22*17) +( numero23*8) + (numero24*11) + (numero25*5)
        res6 = res5-numero26
        tk.Label(text=res5,font=f,fg="Black").grid(row=7, column=3)
        tk.Label(text=res6*10,font=f,fg="Blue").grid(row=8, column=3)
        tk.Label(text=res6*25,font=f,fg="green").grid(row=9, column=3)
        tk.Label(text=res6*50,font=f,fg="Black").grid(row=10, column=3)
        # res6 = f"$ {int(res6):,}".replace(",",".")
# Interfaz
ventana = tk.Tk()
ventana.title("RULA")
ventana.geometry("217x230")
ventana.wm_attributes("-topmost", True) # Mantiene la ventana encima de las demas

f = ("Impact",8)
r = tk.CENTER
w = 9

tituloPLE = tk.Label(text="PLE",font=f).grid(row=1,column=0)
tituloMED = tk.Label(text="MED",font=f).grid(row=2,column=0)
tituloCUA = tk.Label(text="CUA",font=f).grid(row=3,column=0)
tituloCAL = tk.Label(text="CAL",font=f).grid(row=4,column=0)
tituloLIN = tk.Label(text="LIN",font=f).grid(row=5,column=0)
tituloCOL = tk.Label(text="COL", fg="Red", font=f).grid(row=6,column=0)

nu1 = tk.Entry(justify=r,width=w)
nu1.grid(row=1,column=1)
nu2 = tk.Entry(justify=r,width=w)
nu2.grid(row=2,column=1)
nu3 = tk.Entry(justify=r,width=w)
nu3.grid(row=3,column=1)
nu4 = tk.Entry(justify=r,width=w)
nu4.grid(row=4,column=1)
nu5 = tk.Entry(justify=r,width=w)
nu5.grid(row=5,column=1)
nu6 = tk.Entry(justify=r,width=w)
nu6.grid(row=6,column=1)
nu11 = tk.Entry(justify=r,width=w)
nu11.grid(row=1,column=2)
nu12 = tk.Entry(justify=r,width=w)
nu12.grid(row=2,column=2)
nu13 = tk.Entry(justify=r,width=w)
nu13.grid(row=3,column=2)
nu14 = tk.Entry(justify=r,width=w)
nu14.grid(row=4,column=2)
nu15 = tk.Entry(justify=r,width=w)
nu15.grid(row=5,column=2)
nu16 = tk.Entry(justify=r,width=w)
nu16.grid(row=6,column=2)
nu21 = tk.Entry(justify=r,width=w)
nu21.grid(row=1,column=3)
nu22 = tk.Entry(justify=r,width=w)
nu22.grid(row=2,column=3)
nu23 = tk.Entry(justify=r,width=w)
nu23.grid(row=3,column=3)
nu24 = tk.Entry(justify=r,width=w)
nu24.grid(row=4,column=3)
nu25 = tk.Entry(justify=r,width=w)
nu25.grid(row=5,column=3)
nu26 = tk.Entry(justify=r,width=w)
nu26.grid(row=6,column=3)


# bsumar = tk.Button(text=" TOTAL\nPresione Tecla Intro ",command= lambda:validaYSuma(""))
# bsumar.grid(row=0,column = 7, rowspan= 5, sticky=tk.N + tk.S) 
ventana.bind("<Return>", validaYSuma)
ventana.bind("<KP_Enter>", validaYSuma)

#agrego el borrado de datos con la Key DELETE
ventana.bind("<Delete>", limpiarCampos)

ventana.bind("<KeyPress-Down>", focus_next_window) # ("<Return>, o pude ser "<KeyPress-Up>")
ventana.bind("<KeyPress-Up>", focus_prev_window) # ("<Return>, o pude ser "<KeyPress-Up>")

# bBorrar = tk.Button(text="LIMPIAR", command= limpiarCampos)
# bBorrar.grid(row=5,column=7, rowspan = 2, sticky=tk.N + tk.S+tk.E + tk.W) 


ventana.mainloop()