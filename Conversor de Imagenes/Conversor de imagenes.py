import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import customtkinter as ctk


# Configuraciones básicas
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Conversor de Imagenes")
        self.geometry(f"{500}x{400}")

        # Variables
        options_output_format = ["jpeg", "png", "gif", "jpg"]
        self.option_format_var = ctk.StringVar()
        self.option_format_var.set("jpeg")  # Formato de salida predeterminado


        # Creando elementos y Widgets
        self.etiqueta = ctk.CTkLabel(self, text="Seleccione archivos de imagen:", anchor="w")
        self.etiqueta.grid(row=0, column=0, padx=20, pady=(10, 0))
        
        self.output_format = ctk.CTkLabel(self, text="Formato de Salida", anchor="w")
        self.output_format.grid(row=0, column=1, padx=20, pady=(10, 0))

        self.textbox = ctk.CTkTextbox(self, width=250)
        self.textbox.grid(row=1, column=0, padx=(20, 0), pady=(2, 10), sticky="nsew")

        self.Button_seleccionar = ctk.CTkButton(self,text= "Seleccionar", border_width=0, command=self.seleccionar_archivos)
        self.Button_seleccionar.grid(row=2, column=0, padx=(20, 2), pady=(2, 2), sticky="nsew")

        self.option_format = ctk.CTkOptionMenu(self, dynamic_resizing=False,variable=self.option_format_var, values=options_output_format)
        self.option_format.grid(row=1, column=1, padx=20, pady=(20, 10), sticky="n")

        self.Button_convertir = ctk.CTkButton(master=self,text= "Convertir", border_width=0,command=self.convertir)
        self.Button_convertir.grid(row=4, column=0, padx=(20, 2), pady=(2, 2), sticky="nsew")

        

    # Definimos las funciones de la App
    
    @staticmethod     # Uso el decorador para aislar esta función, ya que no necesita acceder a los atributos o elemntos de la Clase pricipal
    def convertir_imagenes(ruta_entrada, ruta_salida, formato_salida):
        formatos_compatibles = {
            "jpeg": "JPEG",
            "jpg": "JPEG",
            "png": "PNG",
            "gif": "GIF"
        }
        formato_pillow = formatos_compatibles.get(formato_salida.lower())
        if formato_pillow:
            try:
                with Image.open(ruta_entrada) as imagen:
                    imagen.convert("RGB").save(ruta_salida, format=formato_pillow)
                print(f"La conversión de {ruta_entrada} se ha completado con éxito.")
            except IOError:
                print(f"No se pudo abrir o guardar la imagen {ruta_entrada}.")
        else:
            print(f"Formato de salida no válido: {formato_salida}")

    def seleccionar_archivos(self):
            rutas_archivos = filedialog.askopenfilenames(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")])
            if rutas_archivos:
                for ruta in rutas_archivos:
                    self.textbox.insert("end", ruta + "\n")

    def convertir(self):
        rutas_entrada = self.textbox.get("1.0", "end").split("\n")
        rutas_entrada = [ruta for ruta in rutas_entrada if ruta.endswith((".png", ".jpg", ".jpeg", ".gif"))]
        formato_salida = self.option_format_var.get()

        for ruta_entrada in rutas_entrada:
            ruta_salida = ruta_entrada.rsplit(".", 1)[0] + "." + formato_salida.lower()
            self.convertir_imagenes(ruta_entrada, ruta_salida, formato_salida)

        self.textbox.delete("1.0", "end")
        messagebox.showinfo("Conversión completada", "La conversión de los archivos se ha completado con éxito.")


 
if __name__ == "__main__":
    app = App()
    app.mainloop()