import customtkinter
from tkintermapview import TkinterMapView
from tkintermapview import utility_functions
from tkinter import messagebox


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


app.title("app")
app.minsize(800, 500)

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
