# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 0-L-4
# PROFESOR DE TEORÍA: ALEJANDRO CISTERNA
# PROFESOR DE LABORATORIO: LUIS RIOS / ALEX MUÑOZ
# GRUPO: 1
# INTEGRANTES
# 1. Ignacio Andres Solar Arce 21.284.189-7
# 2. Vicente Gerardo Arce Palacios 21.538.935-9
# 3. Vicente Aníbal Aninat Norambuena  21.254.766-2
# 4. Ignacio Isaias Celis Castro 21.243.649-6
# 5. Gabriel Alejandro Marin Huerta 21.323.284-3
# 6. Ignacio Vicenzo D'agostino Jara 21.226.101-7
# DESCRIPCIÓN DEL PROGRAMA
'''
Parte 2 del sistema de denuncias de agua.
Que funciona ahora mismo?:
-Sistema de seleccion de entrada entre denunciante o funcionario de SMAPA
-Sistema para agregar marcadores en el mapa que sean solamente en Maipu
- (nuevo) Logeo y limite de marcadores agregado
- checkboxs placeholders para las condiciones de las denuncias
- exportacion de coordenadas en tuple a un csv
- lo unico que falta es cargar los datos a la interfaz de smapa
'''


# BLOQUE DE DEFINICIONES
# ----------------------------------------------------------------------------
# IMPORTACION DE FUNCIONES
# ----------------------------------------------------------------------------
import customtkinter
from tkintermapview import TkinterMapView, utility_functions
import tkinter as tk
import pandas as pd

# ----------------------------------------------------------------------------
menu = customtkinter.CTk()  # Constante inicial para iniciar
# el menu de seleccion
# ----------------------------------------------------------------------------
# DEFINICIONES DE FUNCIONES
'''
Entrada: No tiene entrada.
Descripcion: Funcion principal para la GUI de denuncias de cortes de agua
Salida: GUI con mapa para poder hacer las denuncias
'''


def denunciante():
    # se agregan variables globables para usarlas despues
    global amount
    amount = 0
    global markerpos
    markerpos = []
    '''
    Entrada: No tiene entrada.
    Descripcion: Funcion para analizar la entrada de coordenadas en tuple y
    confirmar si estan dentro de la comuna de maipu via comparacion burda de
    los numeros iniciales del codigo postal (925)
    Salida: Estados descriptivos si es que la postal marcada esta dentro de
    maipu o no, y si lo esta, se agrega el marcador en el mapa
    '''
    def add_marker(cords):
        global amount
        global markerpos
        real = utility_functions.convert_coordinates_to_address(cords[0],
                                                                cords[1])
#        print(real.street, real.housenumber, real.latlng, real.postal)
        if real.postal[0] == "9" and real.postal[1] == "2" and real.postal[2] == "5" and amount == 0:
            markerpos.append(app.map_widget.set_marker(cords[0], cords[1]))
            global latleng
            latleng = real.latlng
#            print(markerpos)
            amount = amount + 1
        elif amount >= 1 and real.postal[0] == "9" and real.postal[1] == "2" and real.postal[2] == "5":
            tk.messagebox.showinfo("Error",
                                   "Ya seleccionaste una posicion para el marcador, debes reiniciar tu seleccion con el boton")
        else:
            tk.messagebox.showinfo("Error",
                                   "El lugar seleccionado no esta en maipu")

    app = customtkinter.CTk()  # Constante inicial para iniciar
    app.geometry("800x500")
    app.title("GUI denuncias de fugas")  # Titulo de la ventana
    # -- bloque de geometria para el mapa
    app.grid_columnconfigure(0, weight=0)
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)
    # -- creamos 2 frame
    # Se le agrega un fondo para que quede igual y no se vea feo
    app.frame_left = customtkinter.CTkFrame(fg_color=None)
    app.frame_left.grid(row=0, column=0)

    app.frame_right = customtkinter.CTkFrame()
    app.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0,
                         sticky="nsew")
    # frame right config
    app.frame_right.grid_rowconfigure(1, weight=1)
    app.frame_right.grid_rowconfigure(0, weight=0)
    app.frame_right.grid_columnconfigure(0, weight=1)

    # -- invocacion de openmaps al grid right
    app.map_widget = TkinterMapView(app.frame_right)
    app.map_widget.grid(row=1, column=0, columnspan=2, sticky="nswe")

    # -- Comando que genera la opcion extra para poder recibir coordenada
    # se relaciona con la deficion add_marker
    app.map_widget.add_right_click_menu_command(label="Añadir un marcador",
                                                command=add_marker,
                                                pass_coords=True)
    # --- defaults map_widget
    app.map_widget.set_address("Maipu")
    app.map_widget.set_zoom(14)

    # -- global stack for checkboxs output
    global is_checked_1
    is_checked_1 = tk.IntVar()
    global is_checked_2
    is_checked_2 = tk.IntVar()
    global is_checked_3
    is_checked_3 = tk.IntVar()
    global is_checked_4
    is_checked_4 = tk.IntVar()
    global is_checked_5
    is_checked_5 = tk.IntVar()
    global is_checked_6
    is_checked_6 = tk.IntVar()

    # --- left config stack o_o
    app.frame_left.grid_rowconfigure(2, weight=1)
    app.titulo = customtkinter.CTkLabel(master=app.frame_left,
                                        text="Parametros de denuncias",
                                        text_font=("Roboto Medium", -16))
    app.titulo.grid(row=0, column=0, pady=10, padx=10)
    app.boton_check = customtkinter.CTkButton(master=app.frame_left,
                                              text="REINICIAR MARCADOR",
                                              command=restart_cordammount)
    app.boton_check.grid(pady=(20, 0), padx=(20, 20), row=8,
                         column=0, sticky="nswe")
    app.boton6 = customtkinter.CTkCheckBox(master=app.frame_left,
                                           text="PLACEHOLDER 6",
                                           onvalue=1, offvalue=0,
                                           variable=is_checked_6)
    app.boton6.grid(row=6, column=0, pady=10, padx=20, sticky="w")
    app.boton5 = customtkinter.CTkCheckBox(master=app.frame_left,
                                           text="PLACEHOLDER 5",
                                           onvalue=1, offvalue=0,
                                           variable=is_checked_5)
    app.boton5.grid(row=5, column=0, pady=10, padx=20, sticky="w")
    app.boton4 = customtkinter.CTkCheckBox(master=app.frame_left,
                                           text="PLACEHOLDER 4",
                                           onvalue=1, offvalue=0,
                                           variable=is_checked_4)
    app.boton4.grid(row=4, column=0, pady=10, padx=20, sticky="w")
    app.boton3 = customtkinter.CTkCheckBox(master=app.frame_left,
                                           text="PLACEHOLDER 3",
                                           onvalue=1, offvalue=0,
                                           variable=is_checked_3)
    app.boton3.grid(row=3, column=0, pady=10, padx=20, sticky="w")
    app.boton2 = customtkinter.CTkCheckBox(master=app.frame_left,
                                           text="PLACEHOLDER 2",
                                           onvalue=1, offvalue=0,
                                           variable=is_checked_2)
    app.boton2.grid(row=2, column=0, pady=10, padx=20, sticky="w")
    app.boton1 = customtkinter.CTkCheckBox(master=app.frame_left,
                                           text="PLACEHOLDER 1",
                                           onvalue=1, offvalue=0,
                                           variable=is_checked_1)
    app.boton1.grid(row=1, column=0, pady=10, padx=20, sticky="w")
    app.boton_check = customtkinter.CTkButton(master=app.frame_left,
                                              text="INGRESAR DENUNCIA",
                                              command=selection)
    app.boton_check.grid(pady=(20, 0), padx=(20, 20), row=7,
                         column=0, sticky="nswe")

    def restart_menu():
        app.destroy()
        starting_menu()
    app.restart = customtkinter.CTkButton(
        master=app.frame_left, text="Volver al menu principal", command=restart_menu)
    app.restart.grid(pady=(20, 0), padx=(20, 20), row=9,
                     column=0, sticky="nswe")
    app.mainloop()

    # end


'''
Entrada: No tiene entrada.
Descripcion: Funcion para registrar datos y exportarlos al csv
Salida: message box de confirmacion y datos exportados
'''


def selection():
    #
    sum = is_checked_1.get() + is_checked_2.get() + is_checked_3.get() + \
        is_checked_4.get() + is_checked_5.get() + is_checked_6.get()
    tk.messagebox.showinfo(
        "Completado", f"{sum} parametros fueron seleccionados y las coordenadas son {latleng}")
    # sublista de cords y la cantidad de checkboxs es lo que nos interesa exportar

    #Elaboracion del dataframe
    export_sum=[]
    export_coord=[]
    export_coord_aux=[]

    export_sum.append(sum)
    export_coord.append(tuple(latleng))
    export_coord_aux.append(export_coord)

    columna1=["Parametros"]
    columna2=["Coordenadas"]
    df_coord=pd.DataFrame(export_coord_aux,columns=columna2)
    df_param=pd.DataFrame(export_sum,columns=columna1)
    df_datos=pd.concat([df_param,df_coord],axis=1)

    #Exportación del dataframe
    df_datos.to_csv("experimental.csv",
              index=False, sep=";", header=False)

'''
Entrada: Cantidad de markers puestos 
Descripcion: registra la cantidad de marcadores puestos y pone como limite 1,
da la opcion de eliminarlo de la lista canvas(tkinter method) para agregar otro
Salida: al usarlo remueve el marcador y el canvas de la lista y la devuelve empty
'''


def restart_cordammount():
    global amount
    global markerpos
    for marker in markerpos:
        marker.delete()
        markerpos = []
    if amount > 0:
        amount = 0


'''
Entrada: No tiene entrada.
Descripcion: Funcion inicial para incializar todo el programa y la GUI de
seleccion de sub interfaces
Salida: Sub-GUI seleccionada dependiendo de quien sea el usuario
'''
def operador():

    '''
    Entrada: No tiene entrada.
    Descripcion: Funcion para invocar todas las coordenadas del csv y 
    su respectivo marcador
    Salida: marcadores tkinter canvas invocados en el frame del mapa
    '''
    def csv_input():
        return #requiere generarlo con cuidado, ya que genera memleak.
    smapa = customtkinter.CTk()
    smapa.geometry("800x500")
    smapa.title("Operador SMAPA")
        # -- bloque de geometria para el mapa
    smapa.grid_columnconfigure(0, weight=0)
    smapa.grid_columnconfigure(1, weight=1)
    smapa.grid_rowconfigure(0, weight=1)
    # -- creamos 2 frame
    # Se le agrega un fondo para que quede igual y no se vea feo
    smapa.frame_left = customtkinter.CTkFrame(fg_color=None)
    smapa.frame_left.grid(row=0, column=0)

    smapa.frame_right = customtkinter.CTkFrame()
    smapa.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0,
                           sticky="nsew")
    # frame right config
    smapa.frame_right.grid_rowconfigure(1, weight=1)
    smapa.frame_right.grid_rowconfigure(0, weight=0)
    smapa.frame_right.grid_columnconfigure(0, weight=1)

    # -- invocacion de openmaps al grid right
    smapa.map_widget = TkinterMapView(smapa.frame_right)
    smapa.map_widget.grid(row=1, column=0, columnspan=2, sticky="nswe")

    # -- Comando que genera la opcion extra para poder recibir coordenada
        # --- defaults map_widget
    smapa.map_widget.set_address("Maipu")
    smapa.map_widget.set_zoom(14)

    smapa.boton_check = customtkinter.CTkButton(master=smapa.frame_left,
                                                text="PLACEHOLDER")
    #placeholder para agregar el comando de csv input
    smapa.boton_check.grid(pady=(20, 0), padx=(20, 20), row=7,
                         column=0, sticky="nswe")
    smapa.mainloop()

def starting_menu():
    menu.geometry("400x200")
    menu.title("Seleccion de Usuario")

    #  MENU INCIAL SNIPPET
    optionmenu = customtkinter.StringVar(value="Selecciona tu usuario")

    '''
    Entrada: Seleccion de GUI a iniciar
    Descripcion: Bloque elif para seleccionar cual GUI iniciar
    Salida: Alguna de las 2 GUIs incializadas en el programa
    '''

    def eleccion_menu(choice):
        if choice == "Denuncias de fugas":
            menu.destroy()  # apaga el mini menu para luego iniciar en otra
            # ventana el menu seleccionado
            customtkinter.CTkToplevel(denunciante())
        if choice == "Operador SMAPA":
            menu.destroy()  # apaga el mini menu para luego iniciar en otra
            # ventana el menu seleccionado
            customtkinter.CTkToplevel(operador())

            # no se hace lo mismo que en la otra ventana ya que aun no hay
            # funcion definida para la GUI de operadores

# -- ComboBox con variable y de master menu (no "app") para elegir la opcion
    choice = customtkinter.CTkComboBox(master=menu,
                                       values=["Operador SMAPA",
                                               "Denuncias de fugas"],
                                       command=eleccion_menu,
                                       variable=optionmenu,
                                       width=200,)
# -- bloque de grid para dejar todo en el centro
    choice.grid(row=0, column=0)
    menu.columnconfigure(0, weight=1)
    menu.rowconfigure(0, weight=1)  # se configura el grid para que la
    # eleccion quede directamente en el centro

    menu.mainloop()
    return


starting_menu()  # Call de la funcion de master menu para empezar todo