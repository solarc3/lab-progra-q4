#first phase to simply display tk with open streetmaps on the window

import customtkinter
from tkintermapview import TkinterMapView

customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    nombre = "mapa"
    ancho = 800
    alto = 500

    def __init__(mapa):
        super().__init__()

        mapa.title(App.nombre)
        mapa.minsize(App.ancho, App.alto)
        mapa.grid_columnconfigure(1, weight=1)
        mapa.grid_rowconfigure(0, weight=1)
        mapa.frame = customtkinter.CTkFrame(master=mapa)
        mapa.frame.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
        mapa.frame.grid_rowconfigure(1, weight=1)
        mapa.frame.grid_columnconfigure(0, weight=1)

        mapa.map_widget = TkinterMapView(mapa.frame)
        mapa.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))


        # Set default values
        mapa.map_widget.set_address("Maipu")
        mapa.mainloop()





if __name__ == "__main__":
    app = App()
    app.start()