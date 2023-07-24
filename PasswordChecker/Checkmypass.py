import tkinter as tk
import customtkinter as ctk
import hashlib
import requests


# Configuraciones básicas para la interfaz
ctk.set_appearance_mode("sys")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Configuraciones d ela ventana principal
        self.geometry("400x450")
        self.title("CheckMyPass")

        #Configuración del grid en la ventana
        self.frame_1 = ctk.CTkFrame(self)
        self.frame_1.pack(pady=20, padx=20, fill="both", expand=True)

        #Configuración de Widgets
        self.entry_1 = ctk.CTkEntry(master=self.frame_1, placeholder_text="Introduce tu Password")
        self.entry_1.pack(pady=10, padx=10)

        self.button = ctk.CTkButton(master=self.frame_1, text= "Verificar", command=None)
        self.button.pack(padx=20,pady=20)





# Funcines de la App
    def request_api_data(query_char):  # Hace el llamado a la API
        url = 'https://api.pwnedpasswords.com/range/' + query_char
        res = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(f"Error Fetching: {res.status_code}, check de API")
        return res


    # Cuenta cuantas veces se ha encontrado la constraseña en la API
    def get_password_leak_count(hashes, hash_to_check):
        hashes = (line.split(":") for line in hashes.text.splitlines())
        for h, count in hashes:
            if h == hash_to_check:
                return count
        return 0


    def pwned_api_check(password):  # Revisa si la contraseña existe en la API
        sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        first5_char, tail = sha1password[:5], sha1password[5:]
        response = request_api_data(first5_char)
        # print(response)
        return get_password_leak_count(response, tail)


    def main(args):
        count = pwned_api_check(args)
        if count:
            print(f'{args} fué encontrado {count} veces, deberías cambiarlo.')
        else:
            print(f'{args} no fué encontrado, Puedes continuar usándolo')


if __name__ == '__main__':
    app = App()
    app.mainloop()