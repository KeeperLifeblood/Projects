import tkinter as tk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import hashlib
import requests


# Configuraciones básicas para la interfaz
ctk.set_appearance_mode("sys")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


# Clase principal de la APP con los widgets
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Configuraciones d ela ventana principal
        self.geometry("300x350")
        self.title("CheckMyPass")
        self.resizable(False, False)

        #Configuración del grid en la ventana
        self.frame_1 = ctk.CTkFrame(self)
        self.frame_1.pack(pady=20, padx=20, fill="both", expand=True)

        #Configuración de Widgets
        # Eticqueta con el logo
        self.logo_label = ctk.CTkLabel(self.frame_1, text="CheckMyPass", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx=20, pady=(20, 10))
        
        self.entry_1 = ctk.CTkEntry(master=self.frame_1, placeholder_text="Introduce tu Password")
        self.entry_1.pack(pady=10, padx=10)

        self.button = ctk.CTkButton(master=self.frame_1, text= "Verificar", command=self.verify_password)
        self.button.pack(padx=20,pady=20)


# Funcines de la App
    def request_api_data(self,query_char):  # Hace el llamado a la API
        url = 'https://api.pwnedpasswords.com/range/' + query_char
        res = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(f"Error Fetching: {res.status_code}, check de API")
        return res


    # Cuenta cuantas veces se ha encontrado la constraseña en la API
    def get_password_leak_count(self,hashes, hash_to_check):
        hashes = (line.split(":") for line in hashes.text.splitlines())
        for h, count in hashes:
            if h == hash_to_check:
                return count
        return 0


    def pwned_api_check(self,password):  # Revisa si la contraseña existe en la API
        sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        first5_char, tail = sha1password[:5], sha1password[5:]
        response = self.request_api_data(first5_char)
        # print(response)
        return self.get_password_leak_count(response, tail)


    def verify_password(self):
            password = self.entry_1.get()
            count = self.pwned_api_check(password)
            if count:
                msg = f"{password} fue encontrada {count} veces, deberías cambiarlo."
                
                CTkMessagebox(title="Contraseña comprometida!", message= msg, icon="warning") 

            else:
                msg2 = f"{password} no fue encontrada, puedes continuar usándolo."
                
                CTkMessagebox(title="Contraseña segura!", message= msg2, icon="check")




if __name__ == '__main__':
    app = App()
    app.mainloop()