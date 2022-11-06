import customtkinter
from tkintermapview import TkinterMapView
from tkintermapview import utility_functions
from tkinter import messagebox

menu = customtkinter.CTk()


def denunciante():

    app = customtkinter.CTk()

    def add_marker(cords):
        real = utility_functions.convert_coordinates_to_address(cords[0], cords[1])
        print(real.street, real.housenumber, real.latlng, real.postal)
        if real.postal[0] == "9" and real.postal[1] == "2" and real.postal[2] == "5":
            app.map_widget.set_marker(cords[0], cords[1])
            print("esta en mmaipu!!!!")
        else:
            messagebox.showinfo("Error","El lugar seleccionado no esta en maipu")
            print("no esta en maipu!!!")

    app.title("UI denuncias de fugas")
    app.geometry("800x500")

    app.grid_columnconfigure(0, weight=0)  # primera columna
    app.grid_columnconfigure(1, weight=1)  # segunda columna
    app.grid_rowconfigure(0, weight=1)  # las filas no cambian
    app.frame = customtkinter.CTkFrame()
    app.frame.grid(row=0, column=1, sticky="nsew")
    app.frame.grid_rowconfigure(1, weight=1)
    app.frame.grid_columnconfigure(0, weight=1)

    app.map_widget = TkinterMapView(app.frame)
    app.map_widget.grid(row=1, column=0, sticky="nswe")
    # direccion default
    app.map_widget.set_address("Maipu")
    app.map_widget.set_zoom(14)
    app.map_widget.add_right_click_menu_command(label="Añadir un marcador",
                                                command=add_marker,
                                                pass_coords=True)

    app.mainloop()
    # end
    return


menu.geometry("400x200")
menu.title("Seleccion de Usuario")

#  MENU INCIAL SNIPPET
optionmenu = customtkinter.StringVar(value="Selecciona tu usuario")
# set initial value
def eleccion_menu(choice):
    if choice == "Denuncias de fugas":
        menu.destroy()
        customtkinter.CTkToplevel(denunciante())
    else:
        messagebox.showinfo("Error","Ventana de Operador aun en desarrollo")


choice = customtkinter.CTkComboBox(master=menu,
                                     values=["Operador SMAPA", "Denuncias de fugas"],
                                     command=eleccion_menu,
                                     variable=optionmenu,
                                     width=200,)


choice.grid(row=0, column=0)
menu.columnconfigure(0, weight=1)
menu.rowconfigure(0, weight=1)  # se configura el grid para que la eleccion quede directamente en el centro

menu.mainloop()
