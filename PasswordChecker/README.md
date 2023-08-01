# CheckMyPass

CheckMyPass es una aplicación segura de verificación de contraseñas que te ayuda a verificar si una contraseña ha sido comprometida en brechas de datos de internet. Utilizando para ello la API "Have I Been Pwned", CheckMyPass permite validar la seguridad de tus contraseñas y te aconsejará tomar medidas apropiadas para mejorar su seguridad en línea...

## Características Clave

    Verificación de Seguridad de Contraseñas: Puedes ingresar tus contraseñas en la aplicación, y CheckMyPass consultará de forma segura la API "Have I Been Pwned" para determinar si la contraseña ha aparecido en alguna brecha de datos conocida de la web.

    Confidencialidad: CheckMyPass asegura la privacidad y confidencialidad de las contraseñas de los usuarios mediante el uso de técnicas estándar de hash. Las contraseñas nunca se envían en texto claro a la API, lo que brinda una forma segura y anónima de verificar su integridad.

    Resultados Claros: La aplicación proporciona resultados claros e informativos, notificando a los usuarios si su contraseña ha sido encontrada en alguna brecha de datos y especificando la cantidad de ocurrencias. Esta información te ayudará a tomar decisiones sobre si debes cambiar tus contraseñas para aumentar la seguridad.

## Instalación

1. Clona este repositorio en tu máquina local:

git clone https://github.com/KeeperLifeblood/Projects/tree/main/PasswordChecker


2. Instala las dependencias requeridas:

pip install customtkinter requests
pip install CTkMessagebox

## Uso

1. Ejecuta la aplicación:

python checkmypass.py

2. Ingresa tu contraseña en el campo proporcionado y haz clic en el botón "Verificar".

3. La aplicación verificará si tu contraseña ha sido comprometida y mostrará un mensaje de advertencia si es así, o un mensaje de seguridad si tu contraseña es segura.

## Requisitos del sistema

- Python 3.6 o superior.
- Bibliotecas: Customtkinter,CTkMessagebox, requests.

## Ejemplos

Aquí hay algunos ejemplos de cómo utilizar la aplicación:



## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.

2. Crea una nueva rama para tus cambios:

git checkout -b mi-nueva-caracteristica

3. Realiza tus cambios y haz commits:

git commit -m "Agrega nueva característica"

4. Haz un push de tus cambios a tu fork:

git push origin mi-nueva-caracteristica

5. Abre una pull request en este repositorio.


## Créditos

- Customtkinter: (https://github.com/salman-ahmad/customtkinter)
- API "Have I Been Pwned": (https://haveibeenpwned.com/API/v3)
- CTkMessagebox:  (https://github.com/Akascape/CTkMessagebox)