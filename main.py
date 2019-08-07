import os
from tkinter import messagebox
from tkinter import *

gui = Tk()
gui.title('PROBLEMA DEL PERIODICO')
gui.geometry("600x450") #Tamano de la ventana

#Titulo
title = Label(gui, text="PROBLEMA DEL PERIODICO", bg="gray", fg="white", font=(16), padx = 5 , pady = 5)
title.pack()

def crear_archivo(n, NOMBRES, MIN_PAG, MAX_PAG, LECTORES):
    s = open('PeriodicoDatos.dzn',"w+")
    s.write('n='+n+';\n')
    s.write('NP='+str(numero_paginas.get())+';\n')
    
    lectores = 'inter=['
    for lector in LECTORES:
        lectores += str(lector.get()) + ','
    lectores += '];\n'
    aux_lectores = lectores.replace(',];', '];')
    s.write(aux_lectores)
    

    num_paginas = 'num_paginas=[|'
    for i in range(int(n)):
        num_paginas += str(MIN_PAG[i].get()) + ',' + str(MAX_PAG[i].get()) + '|'
    num_paginas += '];\n'
    s.write(num_paginas)
    
    s.close()
    
    resultado_minizinc = os.popen('minizinc PeriodicoGenerico.mzn PeriodicoDatos.dzn').read()
    lineas = resultado_minizinc.split('\n')
    elegidos = lineas[0][lineas[0].find('[')+1:lineas[0].find(']')].split(', ')
    num_paginas_elegidos = lineas[1][lineas[1].find('[')+1:lineas[1].find(']')].split(', ')
    num_lectores = lineas[2].split(' = ')[1].split(';')[0]
    
    resultado = 'Temas elegidos: \n\n'
    nombres = ''
    for i in range(len(elegidos)):
        if(elegidos[i]=='true'):
            nombres += str(NOMBRES[i].get()) + ' # Paginas: ' + num_paginas_elegidos[i] + '\n'
    resultado += nombres + '\nPotencial lectores: ' + num_lectores
    
    messagebox.showinfo(message=resultado, title="Resultado")

def crear_inputs(n):
    tema_label = Label(frame_inputs, text="Tema")
    tema_label.grid (row=1, column=1 , padx = 5 , pady = 5)

    min_paginas_label = Label(frame_inputs, text="Número min paginas")
    min_paginas_label.grid (row=1, column=2 , padx = 5 , pady = 5)

    max_paginas_label = Label(frame_inputs, text="Número max paginas")
    max_paginas_label.grid (row=1, column=3 , padx = 5 , pady = 5)

    lectores_label = Label(frame_inputs, text="Lectores")
    lectores_label.grid (row=1, column=4 , padx = 5 , pady = 5)
    
    NOMBRES = []
    MIN_PAG = []
    MAX_PAG = []
    LECTORES = []

    for i in range(int(n)):
        nombre_tema = Entry(frame_inputs, width="10")
        nombre_tema.grid (row=2+i, column=1 , padx = 5 , pady = 5)
        NOMBRES.append(nombre_tema)

        min_paginas = Entry(frame_inputs, width="5")
        min_paginas.grid (row=2+i, column=2 , padx = 5 , pady = 5)
        MIN_PAG.append(min_paginas)

        max_paginas = Entry(frame_inputs, width="5")
        max_paginas.grid (row=2+i, column=3 , padx = 5 , pady = 5)
        MAX_PAG.append(max_paginas)

        lectores = Entry(frame_inputs, width="5")
        lectores.grid (row=2+i, column=4 , padx = 5 , pady = 5)
        LECTORES.append(lectores)


    boton_calcular = Button (frame_inputs , text="CALCULAR" ,command=lambda: crear_archivo(n, NOMBRES, MIN_PAG, MAX_PAG, LECTORES))
    boton_calcular.grid (row=int(n)+2, column=1, padx = 5 , pady = 5)

    frame_inputs.pack()

# Frame de entrada de informacion inicial del problema
frameInfo = Frame(gui)

# Frame para inputs de informacion
frame_inputs = Frame(gui) 

numero_temas_label = Label(frameInfo, text="¿Cuantos temas desea ingresar?")
numero_temas_label.grid (row=1, column=1 , padx = 5 , pady = 5)

numero_temas = Entry(frameInfo, width="5")
numero_temas.grid (row=1, column=2 , padx = 5 , pady = 5)

numero_paginas_label = Label(frameInfo, text="Cantidad de paginas del periodico")
numero_paginas_label.grid (row=2, column=1 , padx = 5 , pady = 5)

numero_paginas = Entry(frameInfo, width="5")
numero_paginas.grid (row=2, column=2 , padx = 5 , pady = 5)

boton_crear = Button (frameInfo , text="CREAR" ,command=lambda: crear_inputs(numero_temas.get()))
boton_crear.grid (row=3, column=1, padx = 5 , pady = 5)

numero_temas.delete(0,END)
numero_temas.insert(0,0)

frameInfo.pack()

gui.mainloop()

