import hashlib
import requests


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
    while True:
        password = input('Escribe "exit" para salir.\npassword: ')

        if password == 'exit':
            break

        main(password)
