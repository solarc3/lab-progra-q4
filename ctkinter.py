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
Parte 1 del sistema de denuncias de agua.
Que funciona ahora mismo?:
-Sistema de seleccion de entrada entre denunciante o funcionario de SMAPA
-Sistema para agregar marcadores en el mapa que sean solamente en Maipu
-- El logeo de coordenadas de marcadores validos sucede via la consola, aun no
-- se dispone de guardar los datos con Pandas a un CSV

'''
# BLOQUE DE DEFINICIONES
# ----------------------------------------------------------------------------
# IMPORTACION DE FUNCIONES
# ----------------------------------------------------------------------------
import customtkinter
from tkintermapview import TkinterMapView
from tkintermapview import utility_functions
from tkinter import messagebox
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

    app = customtkinter.CTk()  # Constante inicial para iniciar
    # el menu de denuncias
    '''
    Entrada: No tiene entrada.
    Descripcion: Funcion para analisar la entrada de coordenadas en tuple y
    confirmar si estan dentro de la comuna de maipu via comparacion burda de
    los numeros iniciales del codigo postal (925)
    Salida: Estados descriptivos si es que la postal marcada esta dentro de
    maipu o no, y si lo esta, se agrega el marcador en el mapa
    '''
    def add_marker(cords):
        real = utility_functions.convert_coordinates_to_address(cords[0],
                                                                cords[1])
        print(real.street, real.housenumber, real.latlng, real.postal)
        if real.postal[0] == "9" and real.postal[1] == "2" and real.postal[2] == "5":
            app.map_widget.set_marker(cords[0], cords[1])
        else:
            messagebox.showinfo("Error",
                                "El lugar seleccionado no esta en maipu")

    app.title("GUI denuncias de fugas")  # Titulo de la ventana
    # -- bloqque de geometria para el mapa
    app.geometry("800x500")
    app.grid_columnconfigure(0, weight=0)  # primera columna
    app.grid_columnconfigure(1, weight=1)  # segunda columna
    app.grid_rowconfigure(0, weight=1)  # las filas no cambian
    app.frame = customtkinter.CTkFrame()
    app.frame.grid(row=0, column=1, sticky="nsew")
    app.frame.grid_rowconfigure(1, weight=1)
    app.frame.grid_columnconfigure(0, weight=1)
    # -- invocacion de openmaps al grid
    app.map_widget = TkinterMapView(app.frame)
    app.map_widget.grid(row=1, column=0, sticky="nswe")
    # -- direccion default de spawn
    app.map_widget.set_address("Maipu")
    app.map_widget.set_zoom(14)
    # -- Comando que genera la opcion extra para poder recibir coordenadas
    # se relaciona con la deficion add_marker
    app.map_widget.add_right_click_menu_command(label="Añadir un marcador",
                                                command=add_marker,
                                                pass_coords=True)

    app.mainloop()
    # end
    return


'''
Entrada: No tiene entrada.
Descripcion: Funcion inicial para incializar todo el programa y la GUI de
seleccion de sub interfaces
Salida: Sub-GUI seleccionada dependiendo de quien sea el usuario
'''


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
        else:
            messagebox.showinfo("Error",
                                "Ventana de Operador aun en desarrollo")
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
